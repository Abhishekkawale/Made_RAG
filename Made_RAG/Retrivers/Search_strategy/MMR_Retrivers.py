from langchain_core.documents import Document
docs = [
    Document(page_content="Cricket is played worldwide and australia iis most sucessfull team of this format."),
    Document(page_content="Hockey is a national game of te india."),
    Document(page_content="Next cricket world cup is in 2027 in south africa"),
    Document(page_content="In 2026 india won many asian game medals. ")
]









from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings   # for embedding

# initialize open ai embedding
embedding_model = OpenAIEmbeddings()

# create a FAISS vector store from the documnets
vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

# enable MMR in the retrival
retriver = vectorstore.as_retriever(
    search_type = "mmr",
    search_kwargs={"k": 2, "lambda_mult" : 1}   # lambda dor diversity balance , we can edit this value. mention between 0-1 only. Below 1 it will give more diversity
)

query = "What is national sport of india?" 
results = retriver.invoke(query)

# print retrived content 
for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...") #truncate for display
