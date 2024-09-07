import streamlit as st
import requests
from PIL import Image

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
    for uploaded_file in uploaded_files:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Uploaded Screenshot: {uploaded_file.name}", use_column_width=True)

        # Store all the uploaded images in to a directory
        image.save(f"./Images/{uploaded_file.name}")
        
        # Placeholder for integration with Multimodal LLM
        # API call to Multimodal LLM to process the image and optional context (replace this with your own LLM call)
        # Assuming we have an API that processes the screenshot and context
        # result = requests.post(LLM_API_URL, files={'image': uploaded_file}, data={'context': context})
        
        # For now, let's simulate a response
        st.write("### Test Case for: ", uploaded_file.name)
        st.write("""
        - **Description**: Testing the [feature] visible in the screenshot.
        - **Preconditions**: Ensure [setup details] are completed before testing.
        - **Steps**:
          1. Step 1: Interact with [UI Element].
          2. Step 2: Click on [Button] to initiate the process.
          3. Step 3: Verify [condition] is met.
        - **Expected Result**: The [result] should be displayed/processed correctly.
        """)

else:
    st.info("Upload screenshots and provide optional context to generate test cases.")

# Footer
st.write("""
---
Developed by Manish Kumar Tailor | Powered by **Multimodal LLMs**
""")

"""
to save to environment variable:
$env:REPLICATE_API_TOKEN = "r8_AITBnQOgHe8RmYaYw7hyVmyNbcWjO0p397Tox"

to get teh api key:
$env:REPLICATE_API_TOKEN
"""