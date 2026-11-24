from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Cricket is often described as a "gentleman's game" wrapped in a game of physical chess.
batsman—with intense team synergy in the field. From the iconic, historic rivalry of The Ashes
(played between England and Australia) to the high-octane global spectacle of the Indian Premier League (IPL),
cricket bridges deep-rooted traditions with cutting-edge modern entertainment.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,   # with 50 we are getting 9 chunks , with 100 er are getting 5 chunks 
    chunk_overlap = 0
)

result = splitter.split_text(text)

print(len(result))
print(result)