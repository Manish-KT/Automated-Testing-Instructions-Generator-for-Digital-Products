import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import HuggingFacePipeline
from langchain.prompts.few_shot import FewShotPromptTemplate

class TestCaseGenerator:
    def __init__(self):
        self.local_llm = self.load_model()
        self.examples = self.get_examples()
        self.prompt = self.setup_prompt()

    def load_model(self):
        tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neox-20b')
        model = AutoModelForCausalLM.from_pretrained(
            'mosaicml/mpt-7b-chat',
            torch_dtype=torch.bfloat16,
            device_map="auto",
            trust_remote_code=True,
        )
        pipe = pipeline('text-generation', model=model, tokenizer=tokenizer, max_new_tokens=200)
        return HuggingFacePipeline(pipeline=pipe)

    def get_examples(self):
        return [
            {"Usecase": "Given a web application with a single login button. Write test scenarios about the login button in the web application?",
             "Test case":
             """
             Feature: Login button

               Scenario: test the login button
                  Given a login button
                   When user clicks on the button
                   Then login should be successful

               Scenario: test the login button
                  Given a login button
                   When user enters invalid credentials and clicks on the login button
                   Then login should not be successful
             """},
            {"Usecase": "Given a REST API which accepts a POST request. Write test scenarios about the API?",
             "Test case":
             """
             Feature: API endpoint

               Scenario: test the API endpoint with valid request
                  Given an API endpoint
                   When user sends a valid request
                   Then a correct response should be recieved

               Scenario: test the API endpoint with empty body
                  Given an API endpoint
                   When user sends a request with empty body
                   Then an error code should be recieved
             """}
        ]

    def setup_prompt(self):
        example_prompt = PromptTemplate(input_variables=["Usecase", "Test case"], template="Usecase: {Usecase}\n{Test case}")
        return FewShotPromptTemplate(
            examples=self.examples,
            example_prompt=example_prompt,
            suffix="Usecase: {input}",
            input_variables=["input"]
        )

    def generate_test_cases(self, context, num_images):
        chain = LLMChain(llm=self.local_llm, prompt=self.prompt)
        
        input_text = f"Given {num_images} screenshots of a digital product"
        if context:
            input_text += f" with the following context: {context}."
        input_text += " Write test cases to verify the functionality shown in the screenshots."

        return chain.run(input_text)

def main(context, num_images):
    generator = TestCaseGenerator()
    test_cases = generator.generate_test_cases(context, num_images)
    return test_cases

if __name__ == "__main__":
    # Example usage
    context = "This is a mobile app for ordering food"
    num_images = 3
    test_cases = main(context, num_images)
    print(test_cases)