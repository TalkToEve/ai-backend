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

from modules.chatbot.personal_information import PersonalInformationUpdater_v1
from modules.chatbot.summary_conversation import SummaryConversation_v1
from modules.chatbot.search_databases import Search_Database_v1
from modules.chatbot.surveys_manager import SurveyManager_v1

class BaseConversationAnalysis(object):
    """
    Base class for conversation analysis modules.
    """

    def __init__(self, ):
        pass

    def run(self):
        """
        Run the analysis.
        """
        raise NotImplementedError
    
class ConversationAnalysis_v1(BaseConversationAnalysis):
    def __init__(self):
        # Model for the conversation analysis
        self.cambalache_model = ChatOpenAI(model_name = 'gpt-3.5-turbo', temperature = CAMBALACHE_TEMPERATURE)
        
        # Personal information updater
        self.personal_information_updater = PersonalInformationUpdater_v1()
        
        # Summary conversation updater
        self.summary_conversation_updater = SummaryConversation_v1()
        pass
    
    def load_personal_information(self, personal_information):
        # Check if personal_information is a string
        if not isinstance(personal_information, str):
            raise TypeError("personal_information must be a string")
        
        self.personal_information_updater.load_personal_information(personal_information)
    
    def load_prompt_personal_information(self, prompt):
        self.personal_information_updater.load_prompt(prompt, self.cambalache_model)
        
    def update_personal_information(self, conversation):
        self.personal_information_updater.update(conversation)
        
    def get_personal_information(self,):
        return self.personal_information_updater.get_information()
    
    def load_prompt_summary_conversation(self, prompt):
        self.summary_conversation_updater.load_prompt(prompt, self.cambalache_model)
        
    def update_summary_conversation(self, n_messages_before, conversation):
        self.summary_conversation_updater.update(n_messages_before, conversation)
        
    def get_summary_conversation(self,):
        return self.summary_conversation_updater.get_information()
    
class ConversationAnalysis_v2(ConversationAnalysis_v1):
    def __init__(self,):
        super().__init__()
        # Model for the conversation analysis
        self.cambalache_model = ChatOpenAI(model_name = 'gpt-3.5-turbo', temperature = CAMBALACHE_TEMPERATURE)
        
        # Personal information updater
        self.personal_information_updater = PersonalInformationUpdater_v1()
        
        # Summary conversation updater
        self.summary_conversation_updater = SummaryConversation_v1()
        
        # Searcher in the database
        self.searcher_db = Search_Database_v1()
        pass

    def load_prompt_search_database(self, prompt):
        self.searcher_db.load_prompt(prompt, self.cambalache_model)
        
    def load_description_search_database(self, description):
        self.searcher_db.load_description(description = description)
        
    def search_database(self, message):
        output = self.searcher_db.search(message)
        return output
    
class ConversationAnalysis_v3(ConversationAnalysis_v2):
    def __init__(self,):
        super().__init__()
        self.survey_manager = SurveyManager_v1()
        
    def load_survey(self, path, survey_id= None):
        if survey_id is None:
            # First we need to obtain the list of surveys
            self.survey_manager.load_list_of_surveys(path)
            number_questions = 0
            # Now we check if there is a survey to answer
            if self.survey_manager.check_if_has_survey_to_answer():
                # Select the survey to answer
                self.survey_manager.select_survey_to_answer()
                # If there is a survey to answer, we load the survey
                self.survey_manager.load_survey()
                # Obtain the number of questions
                number_questions = self.survey_manager.obtain_number_of_questions()
        else:
            self.survey_manager.load_survey(survey_id=survey_id)
            number_questions = self.survey_manager.obtain_number_of_questions()
            
        return number_questions
    
    def obtain_question(self,number_question, return_dict = False):
        return self.survey_manager.obtain_question(number_question, return_dict=return_dict)
    
    def respond_question(self, number_question, answer):
        return self.survey_manager.load_response(number_question, answer)
    
    def save_survey_responses(self,):
        self.survey_manager.save_survey_responses()