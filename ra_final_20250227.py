
from openai_module import generate_text_with_conversation
from prompts import react_system_prompt
from sample_functions import *
from json_helpers import extract_json


#Available actions are:
available_actions = {
    "get_weather": get_weather,
    "get_ibm_aep_boss_name": get_ibm_aep_boss_name
}


# prompt = """
# what is digital marketing?"""

# prompt = "Should I bring umbrella when going out today in Arizona?"

prompt = input("Enter your prompt: ")

messages = [
    {"role": "system", "content": react_system_prompt},
    {"role": "user", "content": prompt},
]

turn_count = 1
max_turns = 5

while turn_count < max_turns:
    print (f"Loop: {turn_count}")
    print("----------------------")

    response = generate_text_with_conversation(messages, model="gpt-4")

    check_valid_response = extract_json(response)

    # Add while loop to make sure the model returns a valid response
    while check_valid_response == None:
        if turn_count > 1 or 'action' in response:
            break
        response = generate_text_with_conversation(messages, model="gpt-4")
        check_valid_response = extract_json(response)

        # For debugging
        """
        print(f"Response from model:\n{response}")
        input("Press Enter to continue...")
        """

    print(response)

    json_function = extract_json(response)

    if json_function:
            function_name = json_function[0]['function_name']
            function_parms = json_function[0]['function_parms']
            if function_name not in available_actions:
                raise Exception(f"Unknown action: {function_name}: {function_parms}")
            print(f" -- running {function_name} {function_parms}")
            action_function = available_actions[function_name]
            #call the function
            result = action_function(**function_parms)
            function_result_message = f"Action_Response: {result}"
            messages.append({"role": "user", "content": function_result_message})
            print(function_result_message)
    else:
         break
    
    turn_count += 1