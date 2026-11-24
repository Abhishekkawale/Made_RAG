# from langchain_text_splitters import CharacterTextSplitter

# text = """
# Cricket is often described as a "gentleman's game" wrapped in a game of physical chess. It balances extreme individual pressure—such as a single bowler staring down a single batsman—with intense team synergy in the field. From the iconic, historic rivalry of The Ashes (played between England and Australia) to the high-octane global spectacle of the Indian Premier League (IPL), cricket bridges deep-rooted traditions with cutting-edge modern entertainment.
# """

# splitter = CharacterTextSplitter(
#     chunk_size = 50,
#     chunk_overlap = 0,
#     separator = ''
# )

# result = splitter.split_text(text)
# print(result)



# This is a second example using loader class. We will load a pdf and performm splitting.

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('splitting.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
     chunk_size = 50,
     chunk_overlap = 0,
     separator = ''
)
result = splitter.split_documents(docs)
print(result)

