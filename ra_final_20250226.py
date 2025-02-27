
from openai_module import generate_text_basic, generate_text_with_conversation
from prompts import react_system_prompt
from sample_functions import get_weather
from json_helpers import extract_json

# Available actions are:
available_actions = {
    "get_weather": get_weather
}

prompt = """
Should I take an umbrella when going out today in Arizona?"""

messages=[
    {"role": "system", "content": react_system_prompt},
    {"role": "user", "content": prompt}
    ]

turn_count = 1
max_turns = 5

# Add while loop to make sure the model returns a valid response
while turn_count < max_turns:
    print(f"Loop: {turn_count}")
    print("-------------------")

    # Add while loop to make sure the model returns a valid response
    while True:

        # Using generate_text_basic
        """
        response = generate_text_basic(prompt,model="gpt-4", system_prompt=react_system_prompt)
        """
        # debugging
        # if turn_count > 1:
        #     print()
        #     print(f"reponse: {response}")
        #     print()
        #     print(f"messages: {messages}")
        #     print()
        #     input("Press Enter to continue...")

        # Using generate_text_with_conversation
        response = generate_text_with_conversation(messages,model="gpt-4")

        if extract_json(response):
            print()
            print(f"Response from model:\n{response}")
            print()
            print("----------END OF MODEL RESPONSE---------")
            print()
            input("Press Enter to continue...")
        else:
            pass

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

        if json_function is not None:
            print()
            print("Extracted JSON function:")
            print(json_function)
            print(f"json_function type: {type(json_function)}")            
            break
        elif turn_count > 1:
            break

    # To execute the function
    if json_function:

        function_name = json_function[0]['function_name']
        function_parms = json_function[0]['function_parms']
        # debugging
        print(f"function_name: {function_name}")
        print(f"function_name type: {type(function_name)}")
        print(f"function_parms: {function_parms}")
        print(f"function_parms type: {type(function_parms)}")
        print()
        print("----------END OF CHECKING WHAT'S BEEN EXTRACTED---------")
        print()        
        input("Press Enter to continue...")

        if function_name not in available_actions:
            raise Exception(f"Unknown action: {function_name}: {function_parms}")
        
        print(f" -- running {function_name} {function_parms}")
        action_function = available_actions[function_name]
        # debugging
        print(f"action_function: {action_function}")
        print()
        input("Press Enter to continue...")

        # Call the function
        # own interpretation 20250225
        """
        result = action_function(function_parms['city'])
        print(result)
        input("Press Enter to continue...")
        """
        result = action_function(**function_parms)
        function_result_message = f"Action_Response: {result}"

        # Append the function result to the messages list
        messages.append({"role": "user", "content": function_result_message})

        print(function_result_message)
        print()
        print("----------Last part of the loop if there is an extracted JSON function.----------")
        print()
        input("Press Enter to continue...")

    else:
        print(f"Final reponse:\n\n{response}")
        break

    turn_count += 1
        