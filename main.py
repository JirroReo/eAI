import os
from utils import skills_options, causes_options, generate_instruction

from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class LLMS:
    def __init__(self):
        load_dotenv()

        self.openAI = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY_PAID"))

    def generate(self, product, topic):
        if product == 'CT':
            prompt = self.generate_prompt_ct(topic)
            return self.openAI.predict(prompt)
            # print(prompt)

    def generate_prompt_ct(self, topic):
        prompt = """
            Options for skills: {},
            Options for causes: {},
            Instruction: {},

            Your returned data must be in this shape:
            ```json
            Title: '',
            Description: '',
            Skills: [],
            Causes: [],
            ```

            ONLY return the data in this shape. If you return anything else, you will be disqualified.
            DO NOT return any text other than the data in this shape.
            """.format(
                skills_options,
                causes_options,
                generate_instruction(topic)
            )

        return prompt

if __name__ == '__main__':
    llm = LLMS()
    # This second arg is the topic,
    # we can take it from frontend and let the llm generate everything else
    print(llm.generate('CT', 'Backoffice Support'))
