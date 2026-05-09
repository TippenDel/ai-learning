from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key = os.getenv("API_KEY")
)

response = client.chat.completions.create(
    model="kr/claude-haiku-4.5",
    messages=[
        {"role": "system", "content": "Отвечай коротко, максимум 3 предложения"},
        {"role": "user", "content": "Что такое RAG в AI?"}
    ]
)

print(response.choices[0].message.content)