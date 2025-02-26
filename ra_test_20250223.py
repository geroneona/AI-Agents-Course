#Hardcoded Agent
from openai_module import generate_text_basic
from prompts import react_system_prompt
from sample_functions import get_weather

prompt = """
Should I take an umbrella when going out today in Arizona?"""

response = generate_text_basic(prompt,model="gpt-4", system_prompt=react_system_prompt)

print(response)

action_object = response[response.find("Action:")+len("Action:"):].strip()

# Convert action_object into dictionary
action_object = eval(action_object)

print("action_object = eval(action_object):")
print(action_object)
print(f"type: {type(action_object)}")
