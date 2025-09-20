
"""
Retriever logic for multi-query and history-aware retrieval.
"""
from app_core.utils.imports import *

def init_retriever():
    """
    Initialize the multi-query retriever using the OpenAI LLM.
    Returns the retriever object.
    """
    st.session_state.retriever = MultiQueryRetriever.from_llm(
        retriever=st.session_state.db.as_retriever(search_kwargs={"k": 4}),
        llm=st.session_state.openai_llm
    )
    return st.session_state.retriever

def init_history_aware_retreiver():
    """
    Initialize the history-aware retriever for context-aware question reformulation.
    Returns the retriever object.
    """
    st.session_state.retriever_prompt = ChatPromptTemplate.from_messages([
        ("system", '''Given a chat history and the latest user question \
                        which might reference context in the chat history, \
                        formulate a standalone question which can be understood. Do NOT answer the \
                        question,just reformulate it if needed and otherwise return it as is.'''),
        MessagesPlaceholder(variable_name='chat_history'),
        ("human", "{input}"),
    ])
    st.session_state.history_aware_retriever = create_history_aware_retriever(
        llm=st.session_state.openai_llm,
        retriever=st.session_state.db.as_retriever(search_kwargs={"k": 4}),
        prompt=st.session_state.retriever_prompt
    )
    return st.session_state.history_aware_retriever
