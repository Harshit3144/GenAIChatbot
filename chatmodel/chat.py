from dotenv import load_dotenv
import os
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2603",
    api_key=os.getenv("MISTRAL_API_TOKEN")   
)

print("_____Press 0 to exit_____")
while True:
    prompt = input("You: ")
    if prompt == "0":
        break
    response = model.invoke(prompt)
    print("Bot: ",response.content)
