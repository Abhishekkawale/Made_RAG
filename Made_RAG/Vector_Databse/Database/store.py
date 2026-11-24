# insstall the required library  --> pip install langchain chromdb openai tiktoken pypdf langchain-openai langchain-community

from langchain_openai import AzureOpenAIEmbeddings
from langchain.vectorstores import Chroma
#This is usefull only when you have openai api. And open ai model

from langchain.schema import Document

#create langchain docs for IPL Players

doc1 = Document(
    page_content="Virat kohli is mmost followed cricketer on this planet and his cover drive is exeptional. His wife name is anushka sharma.",
    metadata={"team": RCB}
)
doc2 = Document(
    page_content="Ms dhoni is known as a fastest wicket keeper in the world. He is a first captain to win 3 ICC trophis. His wife name is sakshi dhoni.",
    metadata={"team : CSK"} 
)
doc3 = Document(
    page_content="Rohit sharma is known for his pull shot. He lives in mumbai. He has registered a highest score in OLD cricket. ",
    metadata={"team : MI"}
)
doc4 = Document(
    page_content="Kl rahul is a all rounder. He can bat at any number in any format of the game. His flick shot is famous.",
    metadata={"team : DC"}
)

docs = [doc1,doc2,doc3, doc4]

vector_store = Chroma(
    embedding_function=OpenAIEmbeddings(),   # api required , can't perfomr here.
    persist_directory="Chroma_db",
    collection_name="sample"
)

# add documents
vector_store.add_documents(docs)    # herre we will get doc ids

#view documents
vectore_store.get(include=['embedding','documents', 'metadatas'])

# search documents
vectore_store.similarity_search(
    query="Who livies in mumbai?",
    k=2     # how many similar result you want 
)

#search with similarity score
vector_store.similarity_search_with_score(
    query="Most followed cricketer?",
    k=2
)

#meta-data fultering
vector_store.similarity_search_with_score(
    query="",
    filter={"team : CSK"}
)

#document update
update_doc1 = Document(
    page_content = " virat kohli was the most failed captain in IPL but he was the most consistent player in this game ",
    metadata={"team : RCB"}
)
vector_store.update_document(documnet_id='See above', Document="updated_doc1")

# delete
vector_store.delete(ids=['insert_id_here'])