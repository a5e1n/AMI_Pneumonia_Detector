import streamlit as st
from app_config import set_page_style

# Apply global styling
set_page_style()

st.markdown(
    """
    <h1 style='text-align:center; color:#0da6a6;'>📊 Model Information</h1>
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    """
    <p style='font-size:18px; color:#ccc; line-height:1.7;'>
    This AI-powered pneumonia detection system is built using <b>MobileNetV2</b>, 
    a lightweight convolutional neural network pretrained on <b>ImageNet</b> and 
    fine-tuned on a curated medical imaging dataset consisting of 
    chest X-ray scans.
    <br><br>
    Unlike traditional classifiers, this model is trained on <b>three classes</b>:
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <ul style='color:#ccc; font-size:17px; line-height:1.8;'>
        <li><b>NORMAL</b> – Healthy lungs</li>
        <li><b>PNEUMONIA</b> – Signs of infection/inflammation</li>
        <li><b>NOT_XRAY</b> – Non-medical images (added to avoid false predictions)</li>
    </ul>
    """,
    unsafe_allow_html=True
)

st.write("---")

# Model Details
st.markdown(
    """
    <h3 style='color:#0da6a6;'>🔧 Model Details</h3>
    <ul style='color:#ccc; font-size:17px; line-height:1.8;'>
        <li><b>Base Model:</b> MobileNetV2</li>
        <li><b>Input Size:</b> 224 × 224 × 3</li>
        <li><b>Number of Classes:</b> 3 (Normal, Pneumonia, Not X-ray)</li>
        <li><b>Loss Function:</b> Categorical Crossentropy</li>
        <li><b>Optimizer:</b> Adam</li>
        <li><b>Training Epochs:</b> 10</li>
        <li><b>Augmentations:</b> rotation, zoom, brightness shift, flips</li>
        <li><b>Final Activation:</b> Softmax</li>
    </ul>
    """,
    unsafe_allow_html=True
)

st.write("---")

# Dataset Summary
st.markdown(
    """
    <h3 style='color:#0da6a6;'>📁 Dataset Summary</h3>
    <p style='color:#ccc; font-size:17px; line-height:1.7;'>
    The model was trained on a structured and balanced dataset:
    </p>
    <ul style='color:#ccc; font-size:17px; line-height:1.8;'>
        <li><b>NORMAL:</b> 1,583 images</li>
        <li><b>PNEUMONIA:</b> 4,273 images</li>
        <li><b>NOT_XRAY:</b> 5,000 images</li>
    </ul>
    """,
    unsafe_allow_html=True
)

st.write("---")

# Final summary
st.markdown(
    """
    <h3 style='color:#0da6a6;'>⚡ Why This Model Is Reliable</h3>
    <p style='color:#ccc; font-size:17px; line-height:1.7;'>
        • Detects incorrect inputs using the NOT_XRAY class.<br>
        • Generalizes well due to balanced splitting (train/val/test).<br>
        • Fast inference thanks to MobileNetV2’s efficiency.<br>
        • Fine-tuned specifically for medical imaging tasks.<br>
    </p>
    """,
    unsafe_allow_html=True
)

st.write("---")

st.markdown(
    "<p style='text-align:center; color:#777;'>© AMI — Ameen Medical Intelligence.</p>",
    unsafe_allow_html=True
)
