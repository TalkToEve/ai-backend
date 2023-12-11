import os 
import sys

#Obtain the path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
# Add the path to the sys.path list
sys.path.append(parent_dir)
sys.path.append(grandparent_dir)

from configurations.config_surveys import SURVEYS_PATH
from configurations.config_user_managers import USERS_LIST_PATH, PATH_USERS_FOLDERS

import json
import pandas as pd

class Surveys_Creator():    
    def __init__(self,):
        self.survey = {}
        
        self.survey_name = ""
        self.survey_date = ""
        
        self.survey_path = SURVEYS_PATH
        self.survey_file = ""
        
    def load_survey(self, survey):
        # Check that filepath is a dictionary, or .json file
        if isinstance(survey, dict):
            self.survey = survey
        elif survey.endswith(".json"):
            with open(survey) as json_file:
                self.survey = json.load(json_file)
        else:
            raise Exception("The filepath must be a dictionary or a .json file")
    
    def create_survey(self, survey_id, survey_name, survey_date):
        self.survey_name = survey_name
        self.survey_date = survey_date
        self.survey_id = survey_id
        
        self.survey['id'] = survey_id
        self.survey['name'] = self.survey_name
        self.survey['date'] = self.survey_date
    
    def add_question(self, question, answers):
        # Check that question is a string
        if not isinstance(question, str):
            raise Exception("The question must be a string")
        # Check that answers is a list
        if not isinstance(answers, list):
            raise Exception("The answers must be a list")
        
        self.survey['question_' + str(len(self.survey) - 2)] = {'question': question, 'answers': answers}
        
    def save_survey(self):
        # Check that the survey has a name and a date
        if self.survey_name == "" or self.survey_date == "":
            raise Exception("The survey must have a name and a date")
        # Save the survey
        self.survey_path = os.path.join(self.survey_path, self.survey_id)
        # Check if the directory exists and if not create it
        if not os.path.exists(self.survey_path):
            os.makedirs(self.survey_path)
        # Save the survey
        self.survey_file = self.survey_id + '.json'
        with open(os.path.join(self.survey_path, self.survey_file), 'w') as outfile:
            json.dump(self.survey, outfile)
    
    def generate_results_table(self,):
        # Here we need to generate a table where every question is a column and every row is a person
        questions_it = list(self.survey.keys())[3:]
        questions = []
        for i in range(len(questions_it)):
            questions.append(self.survey[questions_it[i]]['question'])
        # Generate the table
        table_results = pd.DataFrame(columns=questions)
        
        # Save the table
        table_results.to_csv(os.path.join(self.survey_path, 'results' + '_' + self.survey_id + '.csv'), index=False)
        
    def generate_surveys_folder_users(self,):
        # Here we need to obtain the list of users
        users_dataframe = pd.read_csv(USERS_LIST_PATH)
        # We need to filter the users dataframe
        users_dataframe = users_dataframe[users_dataframe['type'] == 'user']
        # Users lists
        users_list = list(users_dataframe['user'])
        
        for user in users_list:
            path = os.path.join(PATH_USERS_FOLDERS, user, 'surveys')
            # Check that the directory exists and if not create it
            if not os.path.exists(path):
                os.makedirs(path)
            
            # Check if exists the surveys.csv file
            surveys_file = os.path.join(path, 'surveys.csv')
            if not os.path.exists(surveys_file):
                open(surveys_file, 'w').close()
                surveys_dataframe = pd.DataFrame(columns=['survey_id','survey_name', 'survey_date', 'answered'])
            else:
                # Load the file
                surveys_dataframe = pd.read_csv(surveys_file)
            
            # Now we need to check that the survey name and date are not in the dataframe
            if not ((surveys_dataframe['survey_name'] == self.survey_name) & (surveys_dataframe['survey_date'] == self.survey_date)).any():
                df_aux = pd.DataFrame({'survey_id': [self.survey_id],
                                        'survey_name': [self.survey_name], 
                                       'survey_date': [self.survey_date], 
                                       'answered': [False]})
                
                surveys_dataframe = pd.concat([surveys_dataframe, df_aux],axis=0)
                
                # Save the dataframe
                surveys_dataframe.to_csv(surveys_file, index=False)