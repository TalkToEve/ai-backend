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

class Search_Database_v1():
    def __init__(self,):
        # Define the summary
        self.flag_search = False
        self.prompt = None
        self.searcher = None
        self.description = None
        # Define the requiered inputs variables
        self.required_input_variables = ['message','description']
    
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
        self.searcher = LLMChain(llm = model, verbose = False, prompt = prompt)
    
    def load_description(self, description):
        # Check that description is a string
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        
        self.description = description
            
    def search(self, message):
        # Check that the updater is not None
        if self.searcher is None:
            raise ValueError("The searcher has not been loaded")
        
        # Check that the conversation is a string
        if not isinstance(message, str):
            raise TypeError("conversation must be a string")
        
        # Obtain the new personal information
        flag_search = self.searcher.predict(message = message, description = self.description) 
        
        # Convert to int
        if flag_search == "True":
            flag_search = True
        elif flag_search == "False":
            flag_search = False
        else:
            print("flag_search is not True or False")
        return flag_search