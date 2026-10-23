
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌱"
)

st.title("🌱 PlantCare AI")
st.subheader("Plant Disease Detection Assistant")

st.write("Upload a clear photo of a plant leaf.")

st.info("Demo version: AI disease prediction is not enabled yet.")

uploaded_file = st.file_uploader(
    "Upload a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded plant leaf",
             use_container_width=True)
    st.success("Image uploaded successfully!")
    st.write(f"Width: {image.width} pixels")
    st.write(f"Height: {image.height} pixels")

st.subheader("Basic Plant-Care Tips")
st.markdown("""
- Provide suitable sunlight.
- Avoid overwatering.
- Check leaves regularly.
- Consult an agricultural expert if disease is suspected.
""")
