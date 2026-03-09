# FOLLOW STEPS <->
# ollama pull llama3
# python ingest.py
# uvicorn main:app --reload
# http://localhost:8000/ask?question=Quels services propose votre société ?

from fastapi import FastAPI

# LangChain tools
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

app = FastAPI()

# connexion embeddings
embeddings = OllamaEmbeddings(
    model="llama3"
)

# connexion vector DB
db = Chroma(
    persist_directory="./vectordb",
    embedding_function=embeddings
)

# charger LLM depuis Ollama
llm = Ollama(
    model="llama3"
)

# chaine RAG
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever()
)


@app.get("/ask")

def ask(question: str):

    # LangChain va :
    # 1 chercher les docs dans Chroma
    # 2 envoyer au LLM
    # 3 générer réponse

    response = qa_chain.run(question)

    return {
        "question": question,
        "answer": response
    }
