import os
import sys

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)

sys.path.append(parent_dir)
sys.path.append(grandparent_dir)

""" This script is used to upload a new survey and save that like a .json file . """


continue_flag = True

print("Welcome to the survey uploader")
print("Please, enter the name of the survey")
survey_name = input("Survey name: ")
survey_name = survey_name.lower()

# Now the date 
print("Please, enter the date of the survey")
survey_date = input("Survey date: ")
survey_date = survey_date.lower()

# Now the questions
print("Please, enter the questions of the survey")

survey = {'name': survey_name, 'date': survey_date}

it_question = 0
while continue_flag:
    question = input("Survey question: ")
    # Upload the possible answers
    print("Please, enter the possible answers of the question")
    survey_answers = []
    continue_flag_answers = True
    while continue_flag_answers:
        answer = input("Survey answer: ")
        survey_answers.append(answer)
        print("Do you want to add another answer?")
        answer = input("Answer (y/n): ")
        if answer.lower() == "n":
            continue_flag_answers = False
    
    survey['question_' + str(it_question)] = {'question': question, 'answers': survey_answers}
    it_question+=1
    print("Do you want to add another question?")
    answer = input("Answer (y/n): ")
    if answer.lower() == "n":
        continue_flag = False


# Save the survey
import json
path_to_save = os.path.join(grandparent_dir, 'modules/company_surveys/surveys/')
# Check if the directory exists and if not create it
if not os.path.exists(path_to_save):
    os.makedirs(path_to_save)
    
path_to_save = os.path.join(grandparent_dir, 'modules/company_surveys/surveys/' + survey_name + '_' + survey_date + '.json')
# Check if the file exists and if not create it
if not os.path.exists(path_to_save):
    open(path_to_save, 'w').close()
# Save the survey
with open(path_to_save, 'w') as outfile:
    json.dump(survey, outfile)    