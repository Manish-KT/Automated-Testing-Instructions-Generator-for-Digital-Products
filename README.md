# Automated Testing Instructions Generator for Digital Products

## Overview

This project leverages a multimodal Large Language Model (LLM) to generate detailed testing instructions for digital products based on screenshots and optional context. It features a Streamlit-based user interface for easy interaction and a powerful backend for processing and generating instructions.

## Features

- **Streamlit-based UI:**
  - Text input for optional context
  - Multi-image uploader for screenshots
  - Button to trigger instruction generation

- **Backend Processing:**
  - Integration with a multimodal LLM
  - Generation of detailed testing instructions

- **Output:**
  - Test case description
  - Pre-conditions
  - Step-by-step testing instructions
  - Expected results

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/automated-testing-instructions-generator.git
   cd automated-testing-instructions-generator
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## Usage

1. (Optional) Enter context in the text box.
2. Upload screenshots of the digital product.
3. Click "Generate Testing Instructions".
4. View the generated instructions in the Streamlit UI.

## Backend Details

The backend uses a multimodal LLM to process both images and text. Here's a brief overview of the setup:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.llms import HuggingFacePipeline
import torch

# Model and tokenizer setup
tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neox-20b')
model = AutoModelForCausalLM.from_pretrained(
  'mosaicml/mpt-7b-chat',
  torch_dtype=torch.bfloat16,
  device_map="auto"
)

# Pipeline creation
pipe = pipeline('text-generation', model=model, tokenizer=tokenizer)
local_llm = HuggingFacePipeline(pipeline=pipe)
```

## GUI Element Detection

This project integrates UIED for GUI element detection. To use UIED:

1. Replace the Google OCR key in `detect_text/ocr.py` with your own.
2. Run single image testing:
   ```
   python run_single.py
   ```
3. For batch testing:
   ```
   python run_batch.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the creators of the multimodal LLM and UIED used in this project.
- Streamlit for providing an excellent framework for building data apps.

