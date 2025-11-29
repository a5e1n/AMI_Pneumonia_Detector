import streamlit as st
from app_config import set_page_style

# Apply global styling
set_page_style()

# Title
st.markdown(
    """
    <h1 style='text-align:center; color:#0da6a6;'>📊 Model Information</h1>
    """,
    unsafe_allow_html=True
)

st.write("")

# Intro
st.markdown(
    """
    <p style='font-size:18px; color:#ccc; line-height:1.7;'>
    This AI-powered pneumonia detection system is built using the optimized 
    <b>MobileNetV2</b> architecture — a lightweight and efficient convolutional 
    neural network pretrained on <b>ImageNet</b> and fine-tuned on a curated 
    medical chest X-ray dataset.
    <br><br>
    The model is trained to classify images into <b>three medical categories</b>:
    </p>
    """,
    unsafe_allow_html=True
)

# Classes
st.markdown(
    """
    <ul style='color:#ccc; font-size:17px; line-height:1.8;'>
        <li><b>NORMAL</b> – Clear, healthy lungs.</li>
        <li><b>PNEUMONIA</b> – Infected or inflamed lung tissue.</li>
        <li><b>NOT_XRAY</b> – Non-X-ray images added to prevent incorrect predictions.</li>
    </ul>
    """,
    unsafe_allow_html=True
)

st.write("---")

# Model Details
st.markdown(
    """
    <h3 style='color:#0da6a6;'>🔧 Model Architecture</h3>
    <ul style='color:#ccc; font-size:17px; line-height:1.8;'>
        <li><b>Base Model:</b> MobileNetV2 (ImageNet pretrained)</li>
        <li><b>Input Size:</b> 224 × 224 × 3</li>
        <li><b>Classes:</b> 3 (Normal / Pneumonia / Not X-ray)</li>
        <li><b>Loss Function:</b> Categorical Crossentropy</li>
        <li><b>Optimizer:</b> Adam</li>
        <li><b>Training Epochs:</b> 10</li>
        <li><b>Data Augmentation:</b> Rotation, zoom, brightness shift, flips</li>
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
    The model was trained on a well-structured and diverse dataset containing 
    labeled chest X-ray images:
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <ul style='color:#ccc; font-size:17px; line-height:1.8;'>
        <li><b>NORMAL:</b> 1,340 images</li>
        <li><b>PNEUMONIA:</b> 3,875 images</li>
        <li><b>NOT_XRAY:</b> 1,583 images</li>
    </ul>
    """,
    unsafe_allow_html=True
)

st.write("---")

# Why reliable
st.markdown(
    """
    <h3 style='color:#0da6a6;'>⚡ Why This Model Is Reliable</h3>
    <p style='color:#ccc; font-size:17px; line-height:1.7;'>
        • Trained on real medical imaging data.<br>
        • Includes a <b>NOT_XRAY</b> class to prevent misuse and improve safety.<br>
        • Balanced train/validation/test splitting ensures better generalization.<br>
        • Efficient architecture enables <b>fast real-time inference</b>.<br>
        • Fine-tuned specifically for chest X-ray diagnostic support.<br>
    </p>
    """,
    unsafe_allow_html=True
)

st.write("---")

# Footer
st.markdown(
    "<p style='text-align:center; color:#777;'>© AMI — Ameen Medical Intelligence.</p>",
    unsafe_allow_html=True
)
