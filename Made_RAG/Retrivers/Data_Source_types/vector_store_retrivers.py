# imports

from langchain_community.vectorstores import Chroma   # vector store
from langchain_openai import OpenAIEmbeddings   # for embedding
from langchain_core.documents import Document # for docs

# step_1 --> your source docs
documnets = [
    Document(page_content="Virat kolhi is te best batsman in the world. His wife  is bollywood acteress. "),
    Document(page_content="ms dhoni is very close to radhika ambani and he is the fasttest wicket keeper in the world"),
    Document(page_content="rohit sharma is playing for mumbai indians fornlast 16 years and won 5 ipl throphis for the team."),
    Document(page_content="Openai provide most powerfull embedding models")
]

# initialize embedding model
embedding_model = OpenAIEmbeddings()

# creating chroma vector store in memory
vectorstore = Chroma.from_documents(
    documents=documnets,   # adding docs
    embedding=embedding_model,   # model to convert into vectors
    collection_name="my_collection" 
)  

# convert vector store into retriver
retriver = vectorstore.as_retriver(search_kwargs={"k":2})

#query
query="who is virat kohli "
results = retriver.invoke(query)

# print retrived content 
for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...") #truncate for display
