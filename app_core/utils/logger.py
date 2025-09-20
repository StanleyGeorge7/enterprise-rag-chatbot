
"""
Logger utilities for chat and user interaction logging.
"""
from app_core.utils.imports import *

def log_chat(userprompt, response, profanity_flag):
    """
    Log user prompts and AI responses to a file, with profanity flag handling.
    """
    if profanity_flag == False:
        if st.session_state.LOG_USER_INTERACTION == 'YES':
            with open(st.session_state.filename, 'a', encoding='utf-8') as f:
                f.write('\n')
                write_txt = 'USER' + ': ' + str(userprompt) + '\n'
                f.write(write_txt)
                write_txt = 'AI_RESPONSE' + ': ' + str(response['response']) + '\n'
                f.write(write_txt)
    else:
        if st.session_state.LOG_USER_INTERACTION == 'YES':
            with open(st.session_state.filename, 'a', encoding='utf-8') as f:
                f.write('\n')
                write_txt = 'USER' + ': ' + str(userprompt) + '\n'
                f.write(write_txt)
                write_txt = 'AI_RESPONSE' + ': ' + str(response) + '\n'
                f.write(write_txt)
