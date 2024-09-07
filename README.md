# ScreenTest AI

## Automated Test Case Generation from UI Screenshots

ScreenTest AI is an innovative tool that leverages the power of AI to automatically generate test cases from UI screenshots. By combining UI element detection and large language models, it streamlines the process of creating comprehensive test scenarios for digital products.

## Features

- **UI Element Detection**: Automatically identifies UI components from uploaded screenshots.
- **Test Case Generation**: Creates detailed test cases based on detected UI elements and optional context.
- **User-Friendly Interface**: Easy-to-use Streamlit web application for uploading screenshots and viewing results.

## How It Works

1. **Upload Screenshots**: Users can upload multiple screenshots of the digital product they want to test.
2. **Provide Context**: Optional additional information can be provided to enhance test case generation.
3. **UI Analysis**: The system analyzes the screenshots to detect UI elements using computer vision techniques.
4. **Test Case Generation**: Based on the detected UI elements and provided context, the system generates detailed test cases.

## Technologies Used

- **Frontend**: Streamlit
- **UI Element Detection**: [UIED (UI Element Detection)](https://github.com/MulongXie/UIED)
- **Test Case Generation**: LangChain and Large Language Models (based on [this Kaggle notebook](https://www.kaggle.com/code/sapal6/langchain-and-llms-for-automating-software-testing))
- **Image Processing**: OpenCV, Tesseract OCR
- **Language Model**: MPT-7B-Chat (via Hugging Face Transformers)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/screentest-ai.git
   cd screentest-ai
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR:
   - For Windows: Download and install from [here](https://github.com/UB-Mannheim/tesseract/wiki)
   - For MacOS: `brew install tesseract`
   - For Linux: `sudo apt-get install tesseract-ocr`

4. Set up UIED:
   - Follow the installation instructions in the [UIED repository](https://github.com/MulongXie/UIED)

## Usage

1. Start the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload screenshots of your digital product.

4. (Optional) Provide additional context in the text area.

5. Click "Describe Testing Instructions" to generate test cases.

6. View the detected UI elements and generated test cases.

## Project Structure

- `app.py`: Main Streamlit application
- `ui_element_detector.py`: UI element detection logic using UIED
- `test_case_generator.py`: Test case generation logic using LangChain and LLMs
- `requirements.txt`: List of Python dependencies
- `README.md`: This file

## Contributing

Contributions to ScreenTest AI are welcome! Please feel free to submit pull requests, create issues or spread the word.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [UIED](https://github.com/MulongXie/UIED) for providing the UI element detection framework
- [LangChain](https://github.com/hwchase17/langchain) for simplifying the integration of language models
- The authors of the [Kaggle notebook](https://www.kaggle.com/code/sapal6/langchain-and-llms-for-automating-software-testing) on automating software testing with LLMs

## Contact

For any queries or suggestions, please open an issue in this repository or contact the maintainer at [your-email@example.com].

---

Developed by Manish Kumar Tailor | Powered by **Multimodal LLMs**
