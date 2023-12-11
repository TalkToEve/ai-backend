from configurations.config_llm import CAMBALACHE_TEMPERATURE
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

import os
import sys

# Obtain the path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
# Add the path to the sys.path list
sys.path.append(parent_dir)
sys.path.append(grandparent_dir)

class SummaryConversation_v1():
    def __init__(self,):
        # Define the summary
        self.summary = None
        # Define the updater
        self.updater = None
        self.prompt = None
        # Define the requiered inputs variables
        self.required_input_variables = ['n_messages_before', 'conversation']
        
    def load_prompt(self, prompt, model): 
        # Check if prompt is a PromptTemplate
        if not isinstance(prompt, PromptTemplate):
            raise TypeError("prompt must be a PromptTemplate")
        
        #Check that model is in chat_models 
        if not isinstance(model, ChatOpenAI):
            raise TypeError("model must be a ChatOpenAI")
        
        # Check that the prompt has the required input variables
        for required_input_variable in self.required_input_variables:
            if required_input_variable not in prompt.input_variables:
                raise ValueError(f"The prompt must have the input variable {required_input_variable}")
            
        self.prompt = prompt
        
        # Load the prompt
        self.updater = LLMChain(llm = model, verbose = False, prompt = prompt)
        
    def update(self,n_messages_before, conversation):
        # Check that the updater is not None
        if self.updater is None:
            raise ValueError("The updater has not been loaded")
        
        # Check that the conversation is a string
        if not isinstance(conversation, str):
            raise TypeError("conversation must be a string")
        
        # Check that the previous_information is a string
        if not isinstance(n_messages_before, str):
            raise TypeError("n_messages_before must be a string")
        
        # Obtain the new personal information
        self.summary = self.updater.predict(n_messages_before = n_messages_before, conversation = conversation)
        
    def get_information(self):
        return self.summary

