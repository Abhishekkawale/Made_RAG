# from langchain_community.document_loaders import WebBaseLoader
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI()

# prompt = PromptTemplate(
#     template='Answer the folowing ques  \n {ques} from the following text -\n {text}',
#     input_variables=['ques','text']
# )

# parser = StrOutputParser()
# url = "https://www.myntra.com/lingerie-set/exciting+lives/exciting-lives-non-wired-low-rise-lingerie-set/45044002/buy"
# loader = WebBaseLoader(url) 

# docs = loader.load()



# chain = prompt | model | parser

# print(chain.invoke({'ques':'What is the price of the product','text':docs[0].page_content}))




# #by this code we will get the price of the product mentiond in that link. But as we dont have api so it won;'t give us an ouput.

from langchain_community.document_loaders import WebBaseLoader
url = "https://www.myntra.com/lingerie-set/exciting+lives/exciting-lives-non-wired-low-rise-lingerie-set/45044002/buy"
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs)