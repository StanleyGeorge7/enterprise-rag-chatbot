from app_core.utils.imports import *
from app_core.config.init import init
from app_core.database.vector_db import create_vector_database
from app_core.chains.rag_chain import init_rag_chain
from app_core.retrieval.retriever import init_retriever, init_history_aware_retreiver
from app_core.chains.grader import init_grader
from app_core.chains.workflow import create_graph_workflow
from app_core.chains.response import generate_response
from app_core.utils.display import display_response, display_response_static, display_last_response
from app_core.utils.logger import log_chat
from app_core.utils.performance import log_performance

# Additional utility for chat initialization

def Initialize_Chat():
    try:
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
        init()
        create_vector_database()
        init_rag_chain()
        init_retriever()
        init_history_aware_retreiver()
        init_grader()
        create_graph_workflow()
    except:
        st.error('Error in loading the Chatbot. Refresh the webpage and try again!')
