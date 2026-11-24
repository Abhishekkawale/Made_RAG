from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Write a summary of the poem - \n{poem}',
    input_variables=['poem']
)

parser = StrOutputParser()
loader = TextLoader('cricket.txt', encoding='utf-8')
docs = loader.load()

print(type(docs))
print(len(docs))
print(docs[0])

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))




# Good news! Your API key is now being accepted. Your code has moved past the authentication error, and the new error tells us exactly what the problem is.
# The issue is that your OpenAI API account has no credits remaining. This is a billing issue, not a Python or LangChain code error.
# 1. What does error 429 mean?
# Your traceback contains:
# openai.RateLimitError: Error code: 429
# "You have no credits remaining.
# Add credits to continue using the API."


# In this case, 429 means your account has exhausted its API credit balance. It does not necessarily mean you sent too many requests.