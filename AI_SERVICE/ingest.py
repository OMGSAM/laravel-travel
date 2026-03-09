# ingest.py

# LangChain permet de créer facilement des pipelines LLM
from langchain.document_loaders import TextLoader

# Permet de découper les textes en morceaux
from langchain.text_splitter import CharacterTextSplitter

# embeddings = transformation texte → vecteur
from langchain.embeddings import OllamaEmbeddings

# vector database
from langchain.vectorstores import Chroma


# charger fichier texte
loader = TextLoader("knowledge.txt")

documents = loader.load()

# découper le texte pour améliorer la recherche
text_splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

docs = text_splitter.split_documents(documents)

# embeddings via Ollama
embeddings = OllamaEmbeddings(
    model="llama3"
)

# créer la base vectorielle
db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="./vectordb"
)

# sauvegarder
db.persist()

print("Documents indexés dans ChromaDB")
