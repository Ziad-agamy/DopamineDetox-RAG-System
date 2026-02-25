# Dopamine Detox RAG Assistant

A Retrevial-Augmented Generation (RAG) application designed to help you navigate through a dopamine detox. This project uses custom document context (Dopamine Nation) to provide specific, evidence-based answers to your questions about focus, addiction, and habit formation.

## 🚀 Features
- **Local Context**: Uses local PDF data (`dopamine_nation.pdf`) to ground AI responses.
- **Fast Inference**: Powered by **Groq** (Llama 3.1) for lightning-fast answers.
- **Local Embeddings**: Uses **Ollama** (`nomic-embed-text`) for efficient local vector search.
- **Interactive UI**: Clean and modern interface built with **Gradio**.

## 🛠️ Tech Stack
- **LangChain**: Chain orchestration and RAG pipeline.
- **Groq SDK**: High-performance LLM inference.
- **FAISS**: Local vector database for semantic search.
- **Ollama**: Local embedding generation.
- **Gradio**: Web interface.

## 📋 Prerequisites
1. **Groq API Key**: Get one at [console.groq.com](https://console.groq.com/).
2. **Ollama**: Install [Ollama](https://ollama.com/) and pull the embedding model:
   ```bash
   ollama pull nomic-embed-text
   ```

## ⚙️ Installation & Setup

### 1. Clone the Project
```bash
git clone <your-repo-url>
cd RAG
```

### 2. Set Up Virtual Environment
It is recommended to use the included virtual environment setup:
```powershell
python -m venv rag_env
.\rag_env\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory (you can use `.env.example` as a template):
```env
GROQ_API_KEY=your_groq_api_key_here
GROQ=llama-3.1-8b-instant
EMBEDDER=nomic-embed-text
```

## 🏃 Running the App
Once your environment is activated and `.env` is configured, start the server:
```bash
python app.py
```
After running, open the local URL (usually `http://127.0.0.1:7860`) in your browser to start chatting with your guide.

## 📂 Project Structure
- `app.py`: The main entry point for the Gradio interface.
- `config.py`: Handles environment variable loading and model settings.
- `faiss_index/`: Local storage for the processed vector metadata.
- `dopamine_detox.ipynb`: Jupyter Notebook used for processing the PDF and building the initial index.
- `requirements.txt`: List of dependencies.

## 🛡️ Security
The project includes a `.gitignore` to ensure `.env`, `rag_env`, and local vector stores are not uploaded to public repositories.
