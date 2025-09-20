import base64
import streamlit as st
from app_core.config.chat_init import Initialize_Chat
from app_core.utils.display import display_response, display_response_static, display_last_response
from app_core.utils.logger import log_chat
from app_core.chains.response import generate_response
from app_core.utils.performance import log_performance
from better_profanity import profanity
from langchain_core.messages import HumanMessage, AIMessage
import time

st.markdown(
    """
    <style>
    .custom-header {
        width: 100%;
        margin: 0 auto 2rem auto;
        padding: 1.2rem 0;
        background: linear-gradient(90deg, #6EC1E4 0%, #2980B9 100%);
        color: #fff;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        border-radius: 0 0 18px 18px;
        box-shadow: 0 4px 16px rgba(44, 62, 80, 0.10);
        letter-spacing: 2px;
        font-family: 'Segoe UI', 'Arial', sans-serif;
    }
    </style>
    <div class='custom-header'>
        enterprise-rag-chatbot
    </div>
    """,
    unsafe_allow_html=True
)
user_prompt = st.chat_input("Enter your question here")

if 'initialized' not in st.session_state:
    Initialize_Chat()
    display_response()
    st.session_state.initialized = True

# Ensure chat_history is always initialized
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'question_state' not in st.session_state:
    st.session_state.question_state = False

if 'fbk' not in st.session_state:
    st.session_state.fbk = {}

if user_prompt:
    start_time = time.time()
    st.session_state.question_state = True
    lowercase_prompt = user_prompt.lower()
    if lowercase_prompt.find("ennvee") != -1:
        new_user_prompt = user_prompt
    else:
        new_user_prompt = "From ennVee's perspective, " + user_prompt
    try:
        if st.session_state.question_state:
            profanity_flag = False
            if user_prompt is not None:
                if profanity.contains_profanity(user_prompt):
                    profanity_flag = True
                    st.session_state.chat_history.append(HumanMessage(content=profanity.censor(user_prompt, censor_char='*')))
                    st.session_state.chat_history.append(AIMessage(content="I appreciate your enthusiasm! However, to ensure a productive conversation, I kindly ask to avoid using profanity. Could you please rephrase your question?"))
                    display_response()
                    log_chat(user_prompt, AIMessage(content='''I appreciate your enthusiasm! However, to ensure a productive conversation, I kindly ask to avoid using profanity. Could you please rephrase your question?'''), profanity_flag)
                else:
                    st.session_state.chat_history.append(HumanMessage(content=user_prompt))
                    display_response()
                    with st.spinner('Processing...'):
                        st.markdown(
                            """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .stDeployButton {
                visibility: hidden;
            }
            .stApp {
                background-color: #EEEEE !important;
                top:2% !important;
                overflow-x: auto !important;
            }
            .header {
                position: fixed;
                width: 100%;
                text-align: left;
                padding-left: 10px;
                background: #6EC1E4 !important;
                color: white !important;
                top: 0;
                left: 0;
                z-index: 1;
            }
            .header img {
                width: 175px;
                height: 54px;
                }
            .stChatInput {
                flex-grow: 1 !important;
                border: none !important;
                background-color: #e0e0e0 !important;
                outline: none !important;
                font-size: 14px !important;
                transition: background-color 0.3s ease !important;
            }
            .stChatInput:focus {
                background-color: #d4d4d4 !important;
            }
            </style>
            """,
                            unsafe_allow_html=True
                        )
                        response = generate_response({'input': new_user_prompt})
                    display_last_response(response['response'])
                    log_chat(user_prompt, response, profanity_flag)
            else:
                display_response_static()
    except Exception as e:
        st.sidebar.error(e)
        print(e)
    end_time = time.time()
    time_taken = end_time - start_time
    log_performance(time_taken)

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {
        visibility: hidden;
    }
    .stApp {
        background-color: #EEEEE !important;
        top:2% !important;
        overflow-x: auto !important;
    }
    .header {
        position: fixed;
        width: 100%;
        text-align: left;
        padding-left: 10px;
        background: #6EC1E4 !important;
        color: white !important;
        top: 0;
        left: 0;
        z-index: 1;
    }
    .header img {
        width: 175px;
        height: 54px;
        }
    .stChatInput {
        flex-grow: 1 !important;
        border: none !important;
        background-color: #e0e0e0 !important;
        outline: none !important;
        font-size: 14px !important;
        transition: background-color 0.3s ease !important;
    }
    .stChatInput:focus {
        background-color: #d4d4d4 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
