from langchain_classic.chains import RetrievalQA
from langchain_ollama import OllamaEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
import gradio as gr
from config import GROQ, EMBED, GROQ_API_KEY

llm = ChatGroq(model=GROQ, temperature=0.4, api_key=GROQ_API_KEY)
embed = OllamaEmbeddings(model=EMBED)

def generate(input):
    vector_store = FAISS.load_local(
    "faiss_index",
    embed, 
    allow_dangerous_deserialization=True
    )

    rag_template = ChatPromptTemplate.from_template("""\
    Context: {context}
    ____________________________________________________________
    Question: {question}

    Answer the question based ONLY on the context provided above.
    In case the answer is not provided within the context answer with saying "I don't know".\
    """
    )
    
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 4}),
        chain_type_kwargs={
            "verbose": True,
            "prompt": rag_template
        }

    )
    return qa.invoke(input)["result"]

istudy = gr.Interface(
    fn=generate,
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Type your question here..."),
    outputs=gr.Markdown(label="Output"),
    title="Your Guide Through Dopamine Detox"
)
istudy.launch()