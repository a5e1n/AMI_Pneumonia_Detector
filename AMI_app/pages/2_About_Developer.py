import streamlit as st
from app_config import set_page_style
import os

set_page_style()

# ===============================
#       GLOBAL ANIMATION CSS
# ===============================
st.markdown("""
<style>

@keyframes fadeUp {
    0% { opacity: 0; transform: translateY(18px); }
    100% { opacity: 1; transform: translateY(0); }
}

.fade {
    animation: fadeUp 1s ease-out forwards;
}

.fade-1 { animation-delay: 0.2s; }
.fade-2 { animation-delay: 0.5s; }
.fade-3 { animation-delay: 0.8s; }
.fade-4 { animation-delay: 1.1s; }

@keyframes glowPulse {
    0% { box-shadow: 0 0 6px rgba(13,166,166,0.25); }
    50% { box-shadow: 0 0 18px rgba(13,166,166,0.9); }
    100% { box-shadow: 0 0 6px rgba(13,166,166,0.25); }
}

.profile-img {
    border-radius: 14px;
    animation: glowPulse 3s infinite ease-in-out;
}

/* تحسين جودة الصورة (Retina / High Quality) */
img {
    image-rendering: -webkit-optimize-contrast;
    image-rendering: crisp-edges;
    image-rendering: high-quality;
}

.social-block {
    text-align: center;
    margin-bottom: 12px;
}

.social-icon {
    width: 46px;
    margin-bottom: 6px;
    transition: 0.25s;
}

.social-icon:hover {
    transform: scale(1.15);
}

</style>
""", unsafe_allow_html=True)

# ===============================
#           MAIN TITLE
# ===============================
st.markdown("""
<h1 class='fade fade-1' style='text-align:center; color:#0da6a6;'>
    👨🏻‍💻 About the Developer
</h1>
""", unsafe_allow_html=True)

st.write("")

# ===============================
#         PROFILE IMAGE
# ===============================
IMAGE_PATH = "AMI_app/static/my_photo.png"

center = st.columns([1,2,1])[1]
with center:
    if os.path.exists(IMAGE_PATH):

        st.markdown("<div class='profile-wrapper fade fade-2' style='text-align:center;'>",
                    unsafe_allow_html=True)

        st.image(
            IMAGE_PATH,
            width=360,     # 🔥 التكبير + تحسين الوضوح
            caption="Ameen Ali",
            output_format="PNG"
        )

        st.markdown("</div>", unsafe_allow_html=True)

        st.write("")
    else:
        st.error("Developer photo not found.")

st.write("---")

# ===============================
#       NAME + PROFESSIONAL TITLE
# ===============================
st.markdown("""
<div class='fade fade-2' style='text-align:center;'>
    <h2 style='margin-bottom:4px;'>Ameen Ali</h2>
    <p style='font-size:18px; color:#bbb; margin-top:-5px;'>
        Biomedical Engineer • AI Developer • Medical Imaging Specialist
    </p>
</div>
""", unsafe_allow_html=True)

# ===============================
#               ABOUT TEXT
# ===============================
st.markdown("""
<p class='fade fade-3' 
   style='color:#ddd; font-size:17px; line-height:1.7; text-align:justify;'>

I am a Biomedical Engineer with a strong passion for Artificial Intelligence,
medical imaging technologies, and building real-world healthcare solutions that
improve patient outcomes.  
<br><br>
My work focuses on developing AI-powered diagnostic systems that connect 
advanced machine learning techniques with clinical practice.  
<br><br>
This project — the <b>AMI Pneumonia Detection System</b> — represents my commitment
to creating innovative tools that enhance the accuracy, speed, and accessibility
of medical diagnosis.
</p>
""", unsafe_allow_html=True)

st.write("---")

# ===============================
#              SKILLS
# ===============================
st.markdown("""
<h4 class='fade fade-3' style='color:#0da6a6;'>🌟 Core Skills & Expertise</h4>

<ul class='fade fade-3'
    style='color:#ccc; font-size:16px; line-height:1.9;'>
    <li>Deep Learning — CNNs, Grad-CAM visualization</li>
    <li>Medical Imaging — X-ray, CT, MRI analysis</li>
    <li>Biomedical Equipment & System Integration</li>
    <li>Streamlit Web App Development</li>
    <li>Python Programming & Data Processing</li>
</ul>
""", unsafe_allow_html=True)

st.write("---")
st.markdown("""
<div style='text-align:center; padding:30px; color:#00e6e6;'>
    <h3>✨ Entirely developed and engineered by Ameen Ali — Founder & Lead Developer of AMI.
This project represents a fully independent effort from concept to deployment.</h3>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ===============================
#         SOCIAL ICONS — CLEAN
# ===============================
st.markdown("""
<h4 class='fade fade-4' style='color:#0da6a6;'>📬 Contact & Profiles</h4>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

# ==== Instagram ====
with col1:
    st.markdown("""
    <div class="social-block fade fade-4">
        <a href="https://www.instagram.com/a5e1n" target="_blank">
            <img class="social-icon" 
                 src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png">
        </a>
        <p style="color:#ccc; margin:0;">Instagram</p>
        <p style="color:#aaa; font-size:14px; margin-top:-2px;">a5e1n</p>
    </div>
    """, unsafe_allow_html=True)

# ==== Email ====
with col2:
    st.markdown("""
    <div class="social-block fade fade-4">
        <a href="mailto:amenkharsan@gmail.com">
            <img class="social-icon"
                 src="https://cdn-icons-png.flaticon.com/512/552/552486.png">
        </a>
        <p style="color:#ccc; margin:0;">Email</p>
        <p style="color:#aaa; font-size:14px; margin-top:-2px;">amenkharsan@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)

# ==== Phone ====
with col3:
    st.markdown("""
    <div class="social-block fade fade-4">
        <a href="tel:+966537660322">
            <img class="social-icon"
                 src="https://cdn-icons-png.flaticon.com/512/724/724664.png">
        </a>
        <p style="color:#ccc; margin:0;">Phone</p>
        <p style="color:#aaa; font-size:14px; margin-top:-2px;">+966 53 766 0322</p>
    </div>
    """, unsafe_allow_html=True)

# ==== LinkedIn ====
with col4:
    st.markdown("""
    <div class="social-block fade fade-4">
        <a href="https://www.linkedin.com/in/ameen-kharsan-a76745291/" target="_blank">
            <img class="social-icon"
                 src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
        </a>
        <p style="color:#ccc; margin:0;">LinkedIn</p>
        <p style="color:#aaa; font-size:14px; margin-top:-2px;">Profile</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# ===============================
#              FOOTER
# ===============================
st.markdown(
    "<p style='text-align:center; color:#777;'>© AMI — Ameen Medical Intelligence.</p>",
    unsafe_allow_html=True
)
