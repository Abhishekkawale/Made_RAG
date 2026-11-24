from langchain_community.vectorstores import Chroma   # vector store
from langchain_openai import OpenAIEmbeddings   # for embedding
from langchain_core.documents import Document # for docs
from langchain_openai import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever 
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

all_docs = [
    Document(page_content="Cricket is played worldwide and australia iis most sucessfull team of this format.", metadata={"source":"h1"}),
    Document(page_content="Hockey is a national game of te india.", metadata={"source":"h2"}),
    Document(page_content="Next cricket world cup is in 2027 in south africa", metadata={"source":"h3"}),
    Document(page_content="In 2026 india won many asian game medals. ", metadata={"source":"h4"})
]

#initialize openai embedding
embedding_model = OpenAIEmbeddings()

# create faiss vector store 
vectorstore = FAISS.from_documents(documents=all_docs, embedding=embedding_model)

#create retrivers
similarity_retrivers = vectorstore.as_retriever(search_type="similarity", kwargs={"k":3})

#creating multi_query retriver
multiquery_retriver = MultiQueryRetriever.from_llm(
    retriver=vectorstore.as_retriever(search_swargs={"k":3}),
    llm=ChatOpenAI(model="gpt-3.5-turbo")    # whcih llm model do you want to use

)


#query
query="womens world cup?"

#retrive results
similarity_results = similarity_retrivers(query)
multiquery_results = multiquery_retriver(query)


for i, doc in enumerate(similarity_results):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...") #truncate for display

print("*"*150)

for i, doc in enumerate(multiquery_results):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...") #truncate for display

