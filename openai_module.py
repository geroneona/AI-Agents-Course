from openai import OpenAI
import os
from dotenv import load_dotenv
from json_helpers import extract_json

# Load environment variables
load_dotenv()

# Create an instance of the OpenAI class
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define a function that generates text using the OpenAI API
def generate_text_basic(prompt: str, model = "gpt-3.5-turbo", system_prompt: str = "You are a helpfull ai assistant"):
    response = openai_client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
            ]
        )

    # Extract the text from the response
    text_response = response.choices[0].message.content

    # Check if the response contains a JSON function
    if extract_json(text_response):
        print(response)
        print()
        input("Press Enter to continue...")
    else:
        pass

    return text_response



def generate_text_with_conversation(messages,model = "gpt-3.5-turbo"):
    response = openai_client.chat.completions.create(
        model=model,
        messages=messages
        )
    return response.choices[0].message.content


