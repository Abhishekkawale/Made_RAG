#install lib
#!pip install langchain chromadb faiss-cpu openai tiktoken langchain_openai langchain-community wikipedia

from langchain_community.retrievers import WikipediaRetriever

# initialize the retrivals (optional: set lan and top_k)
retriver = WikipediaRetriever(top_k_results=2, lang="en")   # creating obj  

# define your query
query = "the geopolitical history of india and pakistan from the perspective of chinese"

# Get relevant wikipedia doc
docs = retriver.invoke(query)

# print retrived content 
for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...") #truncate for display



# This coe will hit the API of wikipedia and retrive the content for the mentioned query. It wont run here, cause it require a AI model. 