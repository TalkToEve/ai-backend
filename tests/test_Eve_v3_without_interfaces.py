import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(grandparent_dir)

from modules.chatbot.eves import Eve_v3

if __name__ == "__main__":

    # Initialize Eve
    eve = Eve_v3()
    eve.initialize()
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

