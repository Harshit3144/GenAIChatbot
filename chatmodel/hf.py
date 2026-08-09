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


system_msg = SystemMessage(content="answer the user with flirting way")


# keep conversation history
messages = [system_msg]

print("____Press 0 to exit____")
while True:
    user_input = input("You: ")  
    if user_input == "0":
        break
    human_msg = HumanMessage(content=user_input)
    # store the human message to the conversation history
    messages.append(human_msg)
    response = model.invoke(messages) 

    print("\n\nBot: ",response.content, "\n\n")

    # store response in history for future context
    messages.append(response)