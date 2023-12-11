import os
import sys

#Obtain the path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
# Add the path to the sys.path list
sys.path.append(parent_dir)
sys.path.append(grandparent_dir)

from modules.company_surveys.surveys import Surveys_Creator


# Create the survey
survey = Surveys_Creator()
survey_name = "anonymous_health_and_wllbeing_survey_y2"
survey_dat= "2023_12_05"
survey_id = "000"

survey.create_survey(survey_id=survey_id, survey_name=survey_name, survey_date=survey_dat)

survey.load_survey(survey=os.path.join(current_dir, 'surveys', 'anonymous health and wellbeing survey y2 2023_05-12-2023.json'))

survey.save_survey()

survey.generate_results_table()

survey.generate_surveys_folder_users()