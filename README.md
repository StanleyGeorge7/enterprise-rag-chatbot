# Retrieval-Augmented Generation (RAG) Chatbot Project

This project is a modular, industry-standard Streamlit-based chatbot application that leverages LangChain, Pinecone, and OpenAI for Retrieval-Augmented Generation (RAG) and conversational AI. The codebase is organized for maintainability and scalability, with clear separation of configuration, database, chains, retrieval, and utility modules.

## Features

- Modular architecture for easy maintenance and extension
- Streamlit UI for interactive chat
- Pinecone vector database for document retrieval
- OpenAI LLM for answer generation
- Profanity filtering and user interaction logging
- Performance logging (CPU, memory, response time)

## Folder Structure

```
app_core/
  config/        # Configuration and initialization
  database/      # Vector database setup
  chains/        # RAG, grading, workflow, and response logic
  retrieval/     # Retriever logic
  utils/         # Shared utilities (imports, display, logging, performance)
run.py           # Main entry point for Streamlit app
requirements.txt # Python dependencies
```

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/StanleyGeorge7/enterprise-rag-chatbot.git
   cd enterprise-rag-chatbot
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   -fill in your API keys (OpenAI, Pinecone, etc.) in `.env`
4. **Run the app:**
   ```sh
   streamlit run run.py
   ```

## Contributing

- Please add docstrings to all new functions and classes.
- Follow the existing folder structure for new modules.
- Use clear, descriptive commit messages.
