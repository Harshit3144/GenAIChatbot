import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage

load_dotenv()

model = init_chat_model("deepseek-ai/DeepSeek-V4-Flash", api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

system_msg = SystemMessage("You are a helpful assistant.")
human_msg = HumanMessage("Hello, how are you?")

# Use with chat models
messages = [system_msg, human_msg]
response = model.invoke(messages)  # Returns AIMessage

print(response.content)