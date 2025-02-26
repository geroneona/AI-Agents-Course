
from openai_module import generate_text_basic
from prompts import react_system_prompt
from sample_functions import get_weather
from json_helpers import extract_json

# Available actions are:
available_actions = {
    "get_weather": get_weather
}

prompt = """
Should I take an umbrella when going out today in Arizona?"""

response = generate_text_basic(prompt,model="gpt-4", system_prompt=react_system_prompt)

print()
print(f"Response from model:\n{response}")


# Self interpretation 20250223
"""
action_object = response[response.find("Action:")+len("Action:"):].strip()

# Convert action_object into dictionary
action_object = eval(action_object)

print("action_object = eval(action_object):")
print(action_object)
print(f"type: {type(action_object)}")
"""

# Instruct the model to call the action or the function
json_function = extract_json(response)

print()
print("Extracted JSON function:")
print(json_function)
print(f"json_function type: {type(json_function)}")

# To execute the function
if json_function:

    function_name = json_function[0]['function_name']
    function_parms = json_function[0]['function_parms']
    # debugging
    print(f"function_name: {function_name}")
    print(f"function_name type: {type(function_name)}")
    print(f"function_parms: {function_parms}")
    print(f"function_parms type: {type(function_parms)}")
    input("Press Enter to continue...")

    if function_name not in available_actions:
        raise Exception(f"Unknown action: {function_name}: {function_parms}")
    
    print(f" -- running {function_name} {function_parms}")
    action_function = available_actions[function_name]
    # debugging
    print(f"action_function: {action_function}")
    input("Press Enter to continue...")

    # Call the function
    # own interpretation 20250225
    result = action_function(function_parms['city'])
    print(result)
    input("Press Enter to continue...")
    result = action_function(**function_parms)
    function_result_message = f"Action_Response: {result}"
    print(function_result_message)

    