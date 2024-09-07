import streamlit as st
import os
from PIL import Image
from test_case_generator import main as generate_test_cases
from ui_element_detector import main as detect_ui_elements

# Project Title and Description
st.title("ScreenTest AI")
st.subheader("Automated Test Case Generation from UI Screenshots")

st.write("""
### What does ScreenTest AI do?
Upload screenshots of any digital product, provide optional context, and get detailed test cases, including:
- **Preconditions**: What needs to be set up before the test.
- **Testing Steps**: Step-by-step instructions on how to test.
- **Expected Results**: The expected behavior when the test passes.
""")

# Sidebar for Navigation and Input
st.sidebar.header("Input Details")
context = st.sidebar.text_area("Optional Context (Provide any extra information)", "")

# Multi-Image Uploader
uploaded_files = st.file_uploader("Upload Screenshots (PNG/JPG)", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

# Analyze Button
if st.button("Describe Testing Instructions") and uploaded_files:
    # Create a temporary directory to store uploaded images
    if not os.path.exists("./temp_images"):
        os.makedirs("./temp_images")

    for uploaded_file in uploaded_files:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Uploaded Screenshot: {uploaded_file.name}", use_column_width=True)

        # Save the image to the temporary directory
        image_path = f"./temp_images/{uploaded_file.name}"
        image.save(image_path)

    # Detect UI elements
    ui_elements = detect_ui_elements("./temp_images")

    # Display detected UI elements
    st.write("### Detected UI Elements:")
    for element in ui_elements:
        st.write(f"- Type: {element['type']}, Text: {element['text']}")

    # Generate test cases
    test_cases = generate_test_cases(context, len(uploaded_files))

    # Display generated test cases
    st.write("### Generated Test Cases:")
    st.code(test_cases, language="gherkin")

    # Clean up temporary directory
    for file in os.listdir("./temp_images"):
        os.remove(os.path.join("./temp_images", file))
    os.rmdir("./temp_images")

else:
    st.info("Upload screenshots and provide optional context to generate test cases.")

# Footer
st.write("""
---
Developed by Manish Kumar Tailor | Powered by **Multimodal LLMs**
""")