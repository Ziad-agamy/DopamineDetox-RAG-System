from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_experimental.text_splitter import SemanticChunker
from config import EMBED

embed = OllamaEmbeddings(model=EMBED)

path = "dopamine_nation.pdf"
docs = PyPDFLoader(path).load()

text_splitter = SemanticChunker(embed)
docs = text_splitter.split_documents(docs)

vector_store = FAISS.from_documents(
    docs,
    embed,
    distance_strategy="MAX_INNER_PRODUCT",
    normalize_L2=True
).save_local("faiss_index")