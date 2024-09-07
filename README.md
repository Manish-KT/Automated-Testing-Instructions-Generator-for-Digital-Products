# Automated Testing Instructions Generator for Digital Products

## Overview

Welcome to the Automated Testing Instructions Generator project! This tool leverages a multimodal Large Language Model (LLM) to generate detailed testing instructions for digital products based on screenshots and optional context. The project includes both front-end and back-end components, as well as integration with existing GUI element detection tools.

## Features

- **Front-End:**
  - Text box for optional context input.
  - Multi-image uploader for uploading screenshots.
  - Button to trigger the generation of testing instructions.

- **Back-End:**
  - Integration with a multimodal LLM to process images and text.
  - Generation of detailed testing instructions, including:
    - Description of the test case.
    - Pre-conditions.
    - Step-by-step testing instructions.
    - Expected results.

- **Demonstration:**
  - The tool will be demonstrated using the RedBus mobile app (or another app) to generate testing instructions for features like source and destination selection, bus and seat selection, etc.

## Getting Started

### 1. Front-End Development

1. **Setup Input Fields:**
   - **Text Box:** Create a text box for users to input optional context.
   - **Multi-Image Uploader:** Implement functionality to upload multiple screenshots.
   - **Button:** Add a button labeled "Describe Testing Instructions" to trigger instruction generation.

2. **Tools & Technologies:**
   - HTML/CSS/JavaScript for basic implementation.
   - React or Vue.js for dynamic components (optional).

### 2. Back-End Development

1. **Multimodal LLM Integration:**
   - Use a pre-trained multimodal LLM to handle both images and text.
   - **Model Loading:**
     ```python
     from transformers import AutoModelForCausalLM, AutoTokenizer
     import torch

     tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neox-20b')
     model = AutoModelForCausalLM.from_pretrained(
       'mosaicml/mpt-7b-chat',
       torch_dtype=torch.bfloat16,
       device_map="auto"
     )
     ```
   - **Pipeline Creation:**
     ```python
     from transformers import pipeline
     from langchain.llms import HuggingFacePipeline

     pipe = pipeline('text-generation', model=model, tokenizer=tokenizer)
     local_llm = HuggingFacePipeline(pipeline=pipe)
     ```

2. **Prompt Templates:**
   - Create prompts to generate test cases:
     ```python
     from langchain.prompts import PromptTemplate
     from langchain.chains import LLMChain

     prompt_template = PromptTemplate(
       input_variables=["product"],
       template="Given a {product} with a single login button. Write test scenarios about the {product}?"
     )
     chain = LLMChain(llm=local_llm, prompt=prompt_template)
     ```

3. **Integration with UI:**
   - Connect the back-end model with the front-end to process user inputs and generate instructions.

### 3. UIED for GUI Element Detection

1. **Install UIED Dependencies:**
   ```bash
   pip install opencv-python-headless pandas
