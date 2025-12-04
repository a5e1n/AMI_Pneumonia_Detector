import streamlit as st
from app_config import set_page_style

set_page_style()

# ============================
#       PAGE TITLE
# ============================
st.markdown("""
<h1 style='text-align:center; color:#0da6a6;'>⚙️ How AMI Pneumonia Detector Works</h1>
<p style='text-align:center; color:#ccc; font-size:18px;'>
A clear step-by-step explanation of how the entire diagnostic pipeline works.
</p>
""", unsafe_allow_html=True)

st.write("---")

# ============================
#       STEP 1
# ============================
st.markdown("""
### 🩻 **1. Image Upload**
The user uploads a **chest X-ray image** (JPG, JPEG, PNG).  
The system checks file validity and ensures it is safe to process.
""")

# ============================
#       STEP 2
# ============================
st.markdown("""
### **2. Pre-Processing**
Before sending the image to the AI model, the system performs essential steps:

- Converts the image to **RGB format**
- Resizes it to **224 × 224 pixels**
- Normalizes pixel values to **0–1**
- Ensures consistent shape for the neural network

These steps make the input clean and standardized for best model performance.
""")

# ============================
#       STEP 3
# ============================
st.markdown("""
### **3. Deep Learning Model Prediction**
The system uses a **MobileNetV2-based CNN**, fine-tuned on medical X-ray datasets.

The model predicts **one of three classes**:

- ✅ **NORMAL**
- ⚠️ **PNEUMONIA**
- ❌ **NOT_XRAY** (safety class to prevent misuse or wrong images)

The output includes:
- The predicted class  
- The confidence score  
""")

# ============================
#       STEP 4 – Grad-CAM
# ============================
st.markdown("""
### 🔥 **4. Grad-CAM Visualization (How the AI “Sees” the X-ray)**

Grad-CAM is an explainability technique that shows **where the AI focused** when making its decision.

This helps doctors and users understand *why* the model reached a certain prediction.

#### ✅ **How Grad-CAM Works (Simple Explanation)**

1. The model performs a forward pass → predicts a class  
2. We compute the **gradient** of that class score with respect to the last convolution layer  
3. These gradients tell us how important each region in the feature maps is  
4. We combine them to form a **heatmap**  
5. The heatmap is overlaid on the X-ray to show the AI’s focus  

#### 🎯 Interpretation:
- **Red regions** → areas strongly influencing the prediction  
- **Yellow regions** → medium influence  
- **Blue / Low colors** → areas not important to the AI  

Grad-CAM adds **transparency** and makes the AI decision **clinically interpretable**.
""")

# ============================
#       STEP 5
# ============================
st.markdown("""
### **5. Diagnosis Card Rendering**
Based on the model’s result:

- Green glowing card → **NORMAL**
- Red glowing card → **PNEUMONIA**
- Orange glowing card → **NOT_XRAY**

Each diagnosis card shows:
- The class  
- The model confidence  
- A quick visual status bar  

This makes the result easy to read and understand instantly.
""")

# ============================
#       STEP 6
# ============================
st.markdown("""
### **6. Medical Recommendations**
Depending on the diagnosis, the system provides medical guidance:

- For pneumonia → seek medical evaluation, consider CT scan, monitor symptoms  
- For normal lungs → follow-up only if symptoms persist  
- For NOT_XRAY → upload a proper radiograph  

These suggestions help the user understand the next medical step.
""")

# ============================
#       STEP 7
# ============================
st.markdown("""
### 📄 **7. Automatic PDF Report Generation**
AMI generates a **professional medical-style PDF**, including:

- Patient ID  
- Time & date  
- Diagnosis + confidence  
- Class probabilities  
- Original X-ray  
- Grad-CAM heatmap  
- QR code for verification  
- Footer with legal disclaimer  

This PDF is fully ready for hospital use or clinical review.
""")

# ============================
#       STEP 8
# ============================
st.markdown("""
### 🏥 **8. Future PACS & DICOM Integration**
The system is designed for future compatibility with:

- PACS hospital systems  
- DICOM imaging workflows  
- Encrypted hospital-grade pipelines  

This makes AMI scalable for real clinical environments.
""")

st.write("---")

# FOOTER
st.markdown(
    "<p style='text-align:center; color:#777;'>© AMI — Ameen Medical Intelligence.</p>",
    unsafe_allow_html=True
)
