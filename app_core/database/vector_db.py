
"""
Vector database setup for Pinecone.
"""
from app_core.utils.imports import *

def create_vector_database():
    """
    Initialize the Pinecone vector store for document retrieval.
    Returns the database object.
    """
    st.session_state.db = PineconeVectorStore(index_name=st.session_state.index, embedding=OpenAIEmbeddings())
    return st.session_state.db
