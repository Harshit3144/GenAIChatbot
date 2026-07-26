

import os

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint



llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)
model = ChatHuggingFace(llm=llm)

response = model.invoke("list of famous movies from India?")

print(response.content)