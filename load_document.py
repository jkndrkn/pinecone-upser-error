from os import environ
from time import sleep

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import Pinecone as PineconeStore
from pinecone.grpc import PineconeGRPC as PineconeClient

INDEX_NAME = environ["PINECONE_INDEX"]
TRIALS = 50
TEXT_PATH = "my_text.txt"
PINECONE_API_KEY = environ["PINECONE_API_KEY"]

loader = TextLoader(TEXT_PATH)
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

print("docs length:", len(docs))

embedder = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")

for i in range(0, TRIALS):
    print("trial: ", i, flush=True)

    # Explicitly re-create the connection prior to every upsert
    pinecone_client = PineconeClient(api_key=PINECONE_API_KEY)
    PineconeStore._index = pinecone_client.Index(INDEX_NAME)
    PineconeStore.from_documents(docs[:1], embedder, index_name=INDEX_NAME)
