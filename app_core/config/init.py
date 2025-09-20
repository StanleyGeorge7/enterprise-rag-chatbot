
"""
App initialization and environment variable setup.
"""
from app_core.utils.imports import *

def init():
    """
    Load environment variables and initialize session state for the chatbot.
    """
    load_dotenv(override=True)
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ['TAVILY_API_KEY'] = os.getenv("TAVILY_API_KEY")
    os.environ['LLAMA_PARSE_API_KEY'] = os.getenv("LLAMA_PARSE_API_KEY")
    st.session_state.LOG_USER_INTERACTION = os.getenv("LOG_USER_INTERACTION")
    os.environ['PINECONE_API_KEY'] = os.getenv('PINECONE_API_KEY')
    os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGCHAIN_TRACING_V2')
    os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
    os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')
    st.session_state.web_search_tool = TavilySearchResults(k=3)
    st.session_state.openai_llm = ChatOpenAI(api_key=os.environ['OPENAI_API_KEY'], model='gpt-4o-mini', temperature=0)
    st.session_state.grader_llm = ChatOpenAI(api_key=os.environ['OPENAI_API_KEY'], model='gpt-4o-mini', temperature=0)
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if not st.session_state.chat_history:
        st.session_state.chat_history.append(AIMessage(content='''Hey There! My name is Lumina. How can I help you? '''))
    st.session_state.index = 'qa-on-web'
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S%f")
    st.session_state.filename = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32)) + timestamp + '.txt'
    st.session_state.statistics = {'hit': 0, 'memory_usage': 0, 'cpu_usage': 0}
