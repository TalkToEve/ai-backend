import os

# Configuration of the models
CHAT_TEMPERATURE = 0.5
CAMBALACHE_TEMPERATURE = 0.1
OPENAI_API_KEY = "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"
# Model FInetune
FT_NAME = "ft:gpt-3.5-turbo-0613:eve:eve-v1:88FhyNRo"


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# User files paths
USER_PATH = os.path.join(os.getcwd() , 'eve_project' , "documents" , "users")
SESSION_LIST_NAME = "session_list.csv"


DICT_STATES = {0: 'prompt_state_0.txt', 
               1: 'prompt_state_1.txt',
               2: 'prompt_state_2.txt',
               3: 'prompt_state_3.txt',
               4: 'prompt_state_4.txt',}

CONVERSATION_EXAMPLES_PATH = os.path.join(os.getcwd(),'eve_project',"documents","conversations_examples","conversations.txt")
PREDEFINED_MESSAGES = os.path.join(os.getcwd(),'eve_project',"documents","predefined_messages")

# Templates
PERSONAL_INFORMATION_TEMPLATE_PATH = os.path.join(os.getcwd(),'eve_project',"documents","templates","personal_information_template.txt")

# Template of prompts
PROMPTS_PATH = os.path.join(os.getcwd(),'eve_project',"documents","master_prompts")

ENGLISH = False
if ENGLISH:
    SUMMARY_CONVERSATION_PROMPT_PATH = os.path.join(PROMPTS_PATH,"summary_conversations","summary_conversation_prompt_v0_english.txt")
    MODIFIED_PATIENT_MESSAGE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"modified_patient_message","modified_patient_message_prompt_v0_english.txt")
    MODIFIED_EVE_MESSAGE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"modified_eve_message","modified_eve_message_prompt_v0_english.txt")
    STATE_SELECTOR_PROMPT_PATH = os.path.join(PROMPTS_PATH,"state_selector","state_selector_prompt_v0_english.txt")
    MODIFIED_PERSONAL_INFORMATION_PATIENT_PROMPT_PATH = os.path.join(PROMPTS_PATH,"modified_personal_information_patient","modified_personal_information_patient_prompt_v0_english.txt")
    EVE_RESPONSE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"eve_response","eve_response_prompt_english.txt")
    EVE_RESPONSE_FINETUNE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"eve_response","eve_response_finetune_prompt_english.txt")
    ADVICE_STATE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"eve_response","advice_state_prompt_english.txt")
    KEEP_HEARDING_STATE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"eve_response","keep_hearding_state_prompt_english.txt")
    MEDITATE_STATE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"eve_response","meditate_state_prompt_english.txt")
    WARNING_STATE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"eve_response","warning_state_prompt_english.txt")

    # Finetunning
    EVE_PROMPT_SYSTEM_FOR_FINE_TUNNING = os.path.join(PROMPTS_PATH,"eve_response","eve_prompt_system_for_finetunning_english.txt")
else: 
    WARNING_STATE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"eve_response","warning_state_prompt.txt")
    ADVICE_STATE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"eve_response","advice_state_prompt.txt")
    KEEP_HEARDING_STATE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"eve_response","keep_hearding_state_prompt.txt")
    MEDITATE_STATE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"eve_response","meditate_state_prompt.txt")
    EVE_RESPONSE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"eve_response","eve_response_prompt.txt")
    EVE_RESPONSE_FINETUNE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"eve_response","eve_response_finetune_prompt.txt")
    MODIFIED_PERSONAL_INFORMATION_PATIENT_PROMPT_PATH = os.path.join(PROMPTS_PATH,"modified_personal_information_patient","modified_personal_information_patient_prompt_v0.txt")
    STATE_SELECTOR_PROMPT_PATH = os.path.join(PROMPTS_PATH,"state_selector","state_selector_prompt_v0.txt")
    MODIFIED_EVE_MESSAGE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"modified_eve_message","modified_eve_message_prompt_v0.txt")
    MODIFIED_PATIENT_MESSAGE_PROMPT_PATH = os.path.join(PROMPTS_PATH,"modified_patient_message","modified_patient_message_prompt_v0.txt")
    SUMMARY_CONVERSATION_PROMPT_PATH = os.path.join(PROMPTS_PATH,"summary_conversations","summary_conversation_prompt_v0.txt")

    # Finetunning
    EVE_PROMPT_SYSTEM_FOR_FINE_TUNNING = os.path.join(PROMPTS_PATH,"eve_response","eve_prompt_system_for_finetunning_english.txt")