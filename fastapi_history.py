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

history = [
    {"role": "system", "content": "Ты строгий AI ментор. Отвечай коротко, максимум 2 предложения."}
]

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(message: Message):
    history.append({"role": "user", "content": message.text})
    
    response = client.chat.completions.create(
        model="kr/claude-haiku-4.5",
        messages=history
    )
    
    answer = response.choices[0].message.content
    history.append({"role": "assistant", "content": answer})
    
    return {"response": answer, "history_length": len(history)}

@app.get("/history")
def get_history():
    return {"messages": history}

@app.delete("/history")
def clear_history():
    history.clear()
    history.append({"role": "system", "content": "Ты строгий AI ментор. Отвечай коротко, максимум 2 предложения."})
    return {"status": "history cleared"}

