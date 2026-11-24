from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='Books',       #define path
    glob='*.pdf',       # we want all pdf, various types mentioned in hand writen notes
    loader_cls=PyPDFLoader   #this class cause all of these are pdf 
)

docs = loader.load()
docs = loader.lazy_load()    # this will load one data at a time and remove it from memory instantly it is usefull  when you have lots of pdfs 

for documents in docs:        # this is just to show a difference between these loaders
    print(documents.metadata)

# print(len(docs))

# print(docs[0].page_content)
# print(docs[1].metadata)