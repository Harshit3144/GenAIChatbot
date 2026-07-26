from dotenv import load_dotenv
import os
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2603",
    api_key=os.getenv("MISTRAL_API_TOKEN")   
)

response = model.invoke("tell me a full story of movie of rajkumar rao in which he trapped in a building room?")
print(response.content)
