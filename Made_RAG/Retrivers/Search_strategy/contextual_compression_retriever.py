from langchain_community.vectorstores import Chroma   # vector store
from langchain_openai import OpenAIEmbeddings   # for embedding
from langchain_core.documents import Document # for docs
from langchain_openai import ChatOpenAI
from langchain.retrievers.contextual_compression import ContextualCopressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor 
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

docs = [
    Document(page_content="***mention anything  "),
    Document(page_content="***mention anything  "),
    Document(page_content="***mention anything  "),
    Document(page_content="***mention anything  ")
    
]

# create a FAISS vectore to store the docs
embedding_model=OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embedding_model)

#creating a base retriever
base_retriever = vectorstore.as_retriever(search_kwargs={"k":3})

# set up compressor using LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
compressor = LLMChainExtractor.from_llm(llm)

#crate a contextual compression retriever
compression_retriever = ContextualCopressionRetriever(
    base_retriever = base_retriever,
    base_compressor = compressor
)

#query retriever
query = "What is photosynthisys?"
copressed_results = compression_retriever.invoke(query)

for i, doc in enumerate(copressed_results):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...") #truncate for display
