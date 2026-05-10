from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

messages = [
    {"role": "system", "content": "Ты строгий AI ментор. Отвечай максимум 2 предложения. Никогда не говори кто ты и какая ты модель."}
]

print("Чат запущен. Напиши 'выход' чтобы остановить.\n")

while True:
    user_input = input("Ты: ")
    
    if user_input.lower() == "выход":
        print("Пока!")
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="kr/claude-haiku-4.5",
        messages=messages
    )
    
    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})

    print(f"AI: {answer}\n")