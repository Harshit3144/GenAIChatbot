import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm=llm)

print("----Press 0 to exit----")
system_msg = SystemMessage(content="you are lover type person and talk like you are love with someone and express love in poetic way.")
human_msg = HumanMessage(content="\n\n Hello, how are you?\n\n tell me about yourself?")

# Use with chat models
messages = [system_msg, human_msg]
response = model.invoke(messages) 

print(response.content)