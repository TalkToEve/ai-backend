import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)
sys.path.append(grandparent_dir)

from modules.chatbot.eves import Eve_v6

if __name__ == "__main__":

    # Initialize Eve
    eve = Eve_v6()
    
    # Username and password
    username = "bzorzet"
    password = "bzorzet"
    
    # Initialize Eve
    eve.initialize(username=username, password=password)
    
    # Select the ID
    survey_to_do = '000'
    eve.load_surveys(survey_id= survey_to_do)
    
    # Do the survey
    while eve.do_survey:
        # Obtain the question
        question, id_question = eve.get_survey(return_dict = False)
        
        if question == "None" and id_question == "None":
            break
        # Do the question
        #answer = input("Eve:" + question + '\n Answer: ')
        answer = 'a'
        
        abcd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',]
        answer = answer.lower()
        
        # Obtain the index of the answer
        answer_id = abcd.index(answer)
        
        # Response the survey
        eve.response_survey(answer_id, id_question)


    # Define the flag chat
    chat = True
    while chat:
        # Obtain the user message
        message = input("USER: ")
        # Check if the user wants to exit
        if message.lower() == "exit":
            chat = False
        else:
            # Obtain the response of Eve
            eve_message = eve.response(message)
            # Print the response of Eve
            print(f"EVE: {eve_message}")

    # Finalize Eve
    eve.finalize()

