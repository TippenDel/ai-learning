from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import math

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

# Создаём embedding через API
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

# Косинусное сходство — насколько близки два вектора
def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x ** 2 for x in a))
    norm_b = math.sqrt(sum(x ** 2 for x in b))
    return dot / (norm_a * norm_b)

# Загружаем и разбиваем документ
def load_and_split(filepath, chunk_size=100):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

# Поиск по смыслу
def find_relevant(chunks, chunk_embeddings, question):
    question_embedding = get_embedding(question)
    scored = []
    for chunk, embedding in zip(chunks, chunk_embeddings):
        score = cosine_similarity(question_embedding, embedding)
        scored.append((score, chunk))
    scored.sort(reverse=True)
    return [chunk for score, chunk in scored[:3]]

# Ответ
def answer(question, context):
    response = client.chat.completions.create(
        model="kr/claude-haiku-4.5",
        messages=[
            {"role": "system", "content": "Отвечай только на основе контекста."},
            {"role": "user", "content": f"Контекст:\n{context}\n\nВопрос: {question}"}
        ]
    )
    return response.choices[0].message.content

# Запуск
chunks = load_and_split("document.txt")
print(f"Чанков: {len(chunks)}")
print("Создаю embeddings...")

chunk_embeddings = [get_embedding(chunk) for chunk in chunks]
print("Готово\n")

question = "Как модели запоминают информацию?"
relevant = find_relevant(chunks, chunk_embeddings, question)
context = "\n\n".join(relevant)
result = answer(question, context)

print(f"Вопрос: {question}")
print(f"Ответ: {result}")