
"""
Display utilities for Streamlit chat UI.
Functions for rendering chat history and streaming responses.
"""
from app_core.utils.imports import *

def display_response():
    """
    Render the chat history in the Streamlit UI, streaming the latest assistant response.
    """
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if not st.session_state.chat_history:
        st.session_state.chat_history.append(AIMessage(content='''Hey There! My name is Lumina. How can I help you? '''))
    for index, value in enumerate(st.session_state.chat_history):
        if index % 2 == 1:
            message1 = st.chat_message("user", avatar="user.jpg")
            message1.markdown(f'{st.session_state.chat_history[index].content}', unsafe_allow_html=True)
        else:
            if index < len(st.session_state.chat_history) - 1:
                message2 = st.chat_message("assistant", avatar="AI.jpg")
                message2.markdown(f'{st.session_state.chat_history[index].content}', unsafe_allow_html=True)
            else:
                message2 = st.chat_message("assistant", avatar="AI.jpg")
                def stream_data():
                    for word in st.session_state.chat_history[index].content.split(" "):
                        yield word + " "
                        time.sleep(0.02)
                message2.write_stream(stream_data)

def display_response_static():
    """
    Render the chat history in the Streamlit UI without streaming.
    """
    for index, value in enumerate(st.session_state.chat_history):
        if index % 2 == 1:
            message1 = st.chat_message("user", avatar="user.jpg")
            message1.write(st.session_state.chat_history[index].content)
        else:
            if index < len(st.session_state.chat_history) - 1:
                message2 = st.chat_message("assistant", avatar="AI.jpg")
                message2.write(st.session_state.chat_history[index].content)
            else:
                message2 = st.chat_message("assistant", avatar="AI.jpg")
                message2.write(st.session_state.chat_history[index].content)

def display_last_response(answer):
    """
    Stream the last assistant response word by word in the UI.
    """
    message2 = st.chat_message("assistant", avatar="AI.jpg")
    def stream_data():
        for word in answer.split(" "):
            yield word + " "
            time.sleep(0.02)
    message2.write_stream(stream_data)
