import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import os
import cv2
from io import BytesIO
from datetime import datetime
import qrcode

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

from app_config import set_page_style

# رابط تطبيقك في Streamlit (غيّره لو كان مختلف)
APP_URL = "https://ami-pneumonia-detector.streamlit.app"

# ============================================================
#   GLOBAL STYLE
# ============================================================
set_page_style()

# CSS خاص بصندوق التشخيص + عناوين Grad-CAM
st.markdown(
    """
    <style>
    /* ===== Diagnosis Card Base (Teal Medical Background) ===== */
    .diagnosis-card {
        border-radius: 18px;
        padding: 18px 26px;
        margin-top: 18px;
        margin-bottom: 12px;
        text-align: center;
        background: #065b5b;              /* لون طبي ثابت لكل الحالات */
        border: 2px solid #044040;
        color: #f5f5f5;
    }

    .diagnosis-title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
    }

    .diagnosis-subtext {
        font-size: 14px;
        margin: 3px 0;
        opacity: 0.95;
    }

    /* ===== Glow Animations (يتغيّر حسب الحالة) ===== */
    @keyframes glowPulseGreen {
        0%   { box-shadow: 0 0 6px rgba(0, 214, 143, 0.35); }
        50%  { box-shadow: 0 0 22px rgba(0, 214, 143, 1.0); }
        100% { box-shadow: 0 0 6px rgba(0, 214, 143, 0.35); }
    }

    @keyframes glowPulseRed {
        0%   { box-shadow: 0 0 6px rgba(255, 80, 80, 0.35); }
        50%  { box-shadow: 0 0 22px rgba(255, 80, 80, 1.0); }
        100% { box-shadow: 0 0 6px rgba(255, 80, 80, 0.35); }
    }

    @keyframes glowPulseOrange {
        0%   { box-shadow: 0 0 6px rgba(255, 170, 80, 0.35); }
        50%  { box-shadow: 0 0 22px rgba(255, 170, 80, 1.0); }
        100% { box-shadow: 0 0 6px rgba(255, 170, 80, 0.35); }
    }

    .diagnosis-card-normal {
        border-color: rgba(0, 214, 143, 1.0);
        animation: glowPulseGreen 2.4s infinite ease-in-out;
    }

    .diagnosis-card-pneumo {
        border-color: rgba(255, 80, 80, 1.0);
        animation: glowPulseRed 2.4s infinite ease-in-out;
    }

    .diagnosis-card-other {
        border-color: rgba(255, 170, 80, 1.0);
        animation: glowPulseOrange 2.4s infinite ease-in-out;
    }

    .gradcam-title {
        text-align: center;
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 8px;
    }

    .gradcam-caption {
        text-align: center;
        font-size: 13px;
        margin-top: 4px;
        opacity: 0.85;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
#   LOAD MODEL
# ============================================================
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("models/pneumonia_model_3class.keras")

model = load_model()
CLASS_NAMES = ["NORMAL", "NOT_XRAY", "PNEUMONIA"]

# ============================================================
#   GRAD-CAM HELPERS
# ============================================================
def make_gradcam_heatmap(img_array, model, last_conv_layer_name="Conv_1"):
    """
    img_array: shape (1, 224, 224, 3)
    returns 2D heatmap (H, W) in [0,1]
    """
    grad_model = tf.keras.models.Model(
        inputs=model.inputs,
        outputs=[model.get_layer(last_conv_layer_name).output, model.output],
    )

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        class_idx = tf.argmax(predictions[0])
        loss = predictions[:, class_idx]

    grads = tape.gradient(loss, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    conv_outputs = conv_outputs[0]  # (H, W, C)
    heatmap = conv_outputs * pooled_grads  # weight channels
    heatmap = tf.reduce_sum(heatmap, axis=-1)  # (H, W)

    heatmap = tf.maximum(heatmap, 0)
    heatmap /= tf.reduce_max(heatmap) + 1e-8

    return heatmap.numpy()


def build_overlay(original_pil, heatmap, alpha=0.40):
    """
    original_pil: PIL image (any size)
    heatmap: 2D Grad-CAM array in [0,1]
    returns RGB numpy image for display
    """
    heatmap_uint8 = np.uint8(255 * heatmap)
    heatmap_uint8 = cv2.resize(heatmap_uint8, original_pil.size)

    heatmap_color = cv2.applyColorMap(heatmap_uint8, cv2.COLORMAP_JET)
    xray_rgb = np.array(original_pil.convert("RGB"))

    overlay = cv2.addWeighted(xray_rgb, 1 - alpha, heatmap_color, alpha, 0)
    return overlay

# ============================================================
#   PDF REPORT (MEDICAL STYLE + X-RAY + GRAD-CAM + QR)
# ============================================================
def generate_pdf(result_str, confidence, class_probs, original_img, overlay_img):
    """
    Builds a single-page medical-style PDF and returns BytesIO.
    Layout:
      - Header (blue) + logo
      - Patient Result Summary + class probabilities
      - Title: Original X-Ray Image (centered) + X-ray
      - Title: AI Focus Map (Grad-CAM) (centered) + overlay
      - Bottom blue footer + rights + QR (bottom-right)
    """
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # ---------------- HEADER STRIP (TOP) ----------------
    header_h = 80
    c.setFillColorRGB(0.03, 0.20, 0.35)   # dark medical blue
    c.rect(0, height - header_h, width, header_h, fill=1, stroke=0)

    title = "AMI – Pneumonia Detection Report"
    c.setFillColorRGB(1, 1, 1)
    title_font = "Helvetica-Bold"
    title_size = 20
    c.setFont(title_font, title_size)
    title_w = c.stringWidth(title, title_font, title_size)
    c.drawString((width - title_w) / 2, height - header_h + 26, title)

    # Logo (top-right) – صغرناها شوي عشان ما تتداخل مع العنوان
    logo_path = "AMI_app/static/ami_logo.png"
    if os.path.exists(logo_path):
        try:
            c.drawImage(
                logo_path,
                width - 105,
                height - header_h + 8,
                width=80,
                height=55,
                preserveAspectRatio=True,
                mask="auto",
            )
        except Exception:
            pass

    # ---------------- PATIENT SUMMARY ----------------
    margin_left = 50
    y = height - header_h - 30

    patient_id = "AMI-" + datetime.now().strftime("%Y%m%d-%H%M%S")
    now_str = datetime.now().strftime("%Y-%m-%d  %H:%M")

    c.setFillColorRGB(0.1, 0.1, 0.1)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(margin_left, y, "Patient Result Summary")
    y -= 10
    c.setLineWidth(0.7)
    c.setStrokeColorRGB(0.75, 0.75, 0.75)
    c.line(margin_left, y, width - margin_left, y)
    y -= 20

    c.setFont("Helvetica", 11)
    c.drawString(margin_left, y, f"Patient ID: {patient_id}")
    y -= 16
    c.drawString(margin_left, y, f"Report Date & Time: {now_str}")
    y -= 16
    c.drawString(margin_left, y, f"Diagnosis: {result_str}")
    y -= 16
    c.drawString(margin_left, y, f"Model Confidence: {confidence * 100:.2f}%")
    y -= 22

    # Class probabilities
    c.setFont("Helvetica-Bold", 11)
    c.drawString(margin_left, y, "Class probabilities:")
    y -= 16
    c.setFont("Helvetica", 11)
    for name, p in class_probs.items():
        c.drawString(margin_left + 15, y, f"- {name}: {p * 100:.2f}%")
        y -= 14

    # Clinical note
    y -= 8
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColorRGB(0.35, 0.35, 0.35)
    c.drawString(
        margin_left,
        y,
        "Note: This AI result is supportive only and must be interpreted by a qualified clinician.",
    )

    # ---------------- ORIGINAL X-RAY IMAGE SECTION ----------------
    y -= 28
    c.setFillColorRGB(0.1, 0.1, 0.1)
    c.setFont("Helvetica-Bold", 12)
    x_title = width / 2
    c.drawCentredString(x_title, y, "Original X-Ray Image")
    y -= 10
    c.setStrokeColorRGB(0.80, 0.80, 0.80)
    c.setLineWidth(0.6)
    c.line(margin_left, y, width - margin_left, y)
    y -= 18

    if original_img is not None:
        xray_arr = np.array(original_img.convert("RGB"))
        h, w, _ = xray_arr.shape
        max_w = 260
        max_h = 200
        scale = min(max_w / w, max_h / h)
        disp_w = w * scale
        disp_h = h * scale

        img_bytes = BytesIO()
        Image.fromarray(xray_arr).save(img_bytes, format="PNG")
        img_bytes.seek(0)
        img_reader = ImageReader(img_bytes)

        x_img = (width - disp_w) / 2
        y_img = y - disp_h
        c.drawImage(
            img_reader,
            x_img,
            y_img,
            width=disp_w,
            height=disp_h,
            mask="auto",
        )
        y = y_img - 22

    # ---------------- GRAD-CAM SECTION ----------------
    if overlay_img is not None:
        c.setFillColorRGB(0.1, 0.1, 0.1)
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(x_title, y, "AI Focus Map (Grad-CAM)")
        y -= 10
        c.setStrokeColorRGB(0.80, 0.80, 0.80)
        c.setLineWidth(0.6)
        c.line(margin_left, y, width - margin_left, y)
        y -= 18

        h2, w2, _ = overlay_img.shape
        max_w2 = 260
        max_h2 = 200
        scale2 = min(max_w2 / w2, max_h2 / h2)
        disp_w2 = w2 * scale2
        disp_h2 = h2 * scale2

        ov_bytes = BytesIO()
        Image.fromarray(overlay_img).save(ov_bytes, format="PNG")
        ov_bytes.seek(0)
        ov_reader = ImageReader(ov_bytes)

        x_img2 = (width - disp_w2) / 2
        y_img2 = y - disp_h2
        c.drawImage(
            ov_reader,
            x_img2,
            y_img2,
            width=disp_w2,
            height=disp_h2,
            mask="auto",
        )
        y = y_img2 - 20

    # ---------------- FOOTER STRIP (BOTTOM) + RIGHTS + QR ----------------
    footer_h = 35
    c.setFillColorRGB(0.03, 0.20, 0.35)   # نفس لون الهيدر
    c.rect(0, 0, width, footer_h, fill=1, stroke=0)

    c.setFont("Helvetica-Oblique", 8.5)
    c.setFillColorRGB(1, 1, 1)
    rights_text = "© AMI — Ameen Medical Intelligence. This automated report does not replace clinical diagnosis."
    rights_w = c.stringWidth(rights_text, "Helvetica-Oblique", 8.5)
    c.drawString((width - rights_w) / 2, 12, rights_text)

    # QR في الركن السفلي الأيمن يفتح موقعك
    qr = qrcode.QRCode(box_size=2, border=1)
    qr.add_data(APP_URL)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_buf = BytesIO()
    qr_img.save(qr_buf, format="PNG")
    qr_buf.seek(0)
    qr_reader = ImageReader(qr_buf)
    c.drawImage(qr_reader, width - 80, 5, width=50, height=50, mask="auto")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# ============================================================
#   PAGE TITLE
# ============================================================
st.markdown(
    """
    <h1 style='text-align:center; color:#f5f5f5;'>Pneumonia Detection 🔍+ Grad-CAM</h1>
    <h4 style='text-align:center; color:#e0e0e0;'>Developed by: <b>Ameen Ali</b></h4>
    """,
    unsafe_allow_html=True,
)
st.write("")

# ============================================================
#   FILE UPLOAD
# ============================================================
uploaded_file = st.file_uploader(
    "Upload a chest X-ray image:", type=["jpg", "jpeg", "png"]
)

# ============================================================
#   MAIN LOGIC
# ============================================================
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    # صورة الأشعة – بالنص وبحجم أقل شوي
    xray_col = st.columns([1, 12, 1])[1]
    with xray_col:
        st.image(image, caption="Uploaded X-Ray", width=600)

    # زر التحليل في النص تحت الصورة
    col_btn = st.columns([1, 1, 1])
    with col_btn[1]:
        analyze = st.button("Analyze Image 🔍", use_container_width=True)

    if analyze:
        # ---------- Preprocess ----------
        img_resized = image.resize((224, 224))
        img_array = np.expand_dims(np.array(img_resized) / 255.0, axis=0)

        # ---------- Prediction ----------
        preds = model.predict(img_array)[0]
        class_index = int(np.argmax(preds))
        confidence = float(preds[class_index])
        result = CLASS_NAMES[class_index]
        class_probs = {CLASS_NAMES[i]: float(preds[i]) for i in range(3)}

        st.write("---")

        # ---------- Diagnosis Card ----------
        if result == "NORMAL":
            diag_class = "diagnosis-card-normal"
        elif result == "PNEUMONIA":
            diag_class = "diagnosis-card-pneumo"
        else:
            diag_class = "diagnosis-card-other"

        diagnosis_html = f"""
        <div class="diagnosis-card {diag_class}">
            <div class="diagnosis-title">
                 <span>Diagnosis Result</span>
            </div>
            <div class="diagnosis-subtext">Diagnosis: <b>{result}</b></div>
            <div class="diagnosis-subtext">Model Confidence: {confidence * 100:.2f}%</div>
        </div>
        """
        st.markdown(diagnosis_html, unsafe_allow_html=True)

        # شريط الحالة القصير
        if result == "NORMAL":
            st.success("✔ Lungs Appear Normal")
        elif result == "PNEUMONIA":
            st.error("⚠ Pneumonia Detected")
        else:
            st.warning("⚠ This is not a chest X-ray image.")

        # ---------- Grad-CAM ----------
        overlay_img = None
        if result in ["NORMAL", "PNEUMONIA"]:
            heatmap = make_gradcam_heatmap(img_array, model)
            overlay_img = build_overlay(image, heatmap)

            st.write("---")
            st.markdown("<div class='gradcam-title'>AI Focus Map (Grad-CAM)</div>", unsafe_allow_html=True)

            grad_col = st.columns([1, 12, 1])[1]
            with grad_col:
                st.image(overlay_img, caption="", width=600)

            st.markdown(
                "<div class='gradcam-caption'>AI Focus Map (X-ray + Heatmap)</div>",
                unsafe_allow_html=True,
            )

        # ---------- Recommendations ----------
        st.write("---")
        if result == "PNEUMONIA":
            st.info(
                """
                ### 📌 Recommendations:
                - Consult a healthcare provider immediately.
                - CT scan may be needed for confirmation.
                - Follow all prescribed medications.
                - Monitor symptoms such as fever, cough, and shortness of breath.
                """
            )
        elif result == "NORMAL":
            st.info(
                """
                ### 📌 Recommendations:
                - No pneumonia indicators detected.
                - If symptoms persist, consider a follow-up X-ray.
                - Maintain healthy respiratory habits and avoid smoking exposure.
                """
            )
        else:
            st.warning(
                """
                ### 📌 Recommendations:
                - Please upload a proper chest radiograph.
                - Random photos, logos, or documents are not valid inputs.
                """
            )

        # ---------- PDF (ONLY for real X-rays) ----------
        st.write("---")
        if result in ["NORMAL", "PNEUMONIA"]:
            pdf_file = generate_pdf(result, confidence, class_probs, image, overlay_img)
            st.download_button(
                label="📄 Download Medical PDF Report",
                data=pdf_file,
                file_name="AMI_pneumonia_report.pdf",
                mime="application/pdf",
            )

# ============================================================
#   FOOTER (ONE LOGO – BOTTOM)
# ============================================================
st.write("---")
c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    if os.path.exists("AMI_app/static/ami_logo.png"):
        st.image("AMI_app/static/ami_logo.png")

st.markdown(
    "<p style='text-align:center; color:#777;'>© AMI — Ameen Medical Intelligence.</p>",
    unsafe_allow_html=True,
)
