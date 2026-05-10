from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os   

load_dotenv()

app = FastAPI()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

class Message(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/chat")
def chat(message: Message):
    response = client.chat.completions.create(
        model="kr/claude-haiku-4.5",
        messages=[
            {"role": "system", "content": "Отвечай коротко и по делу."},
            {"role": "user", "content": message.text}
        ]
    )
    return {"response": response.choices[0].message.content}