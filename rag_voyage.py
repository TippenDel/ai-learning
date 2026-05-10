from openai import OpenAI
from dotenv import load_dotenv
import voyageai
import time
import os
import math

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

voyage = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))

# Создаём embedding через Voyage AI
# def get_embedding(text):
#     result = voyage.embed([text], model="voyage-3-lite")
#     return result.embeddings[0]

# Создаём embeddings для всех чанков за один запрос
def get_embeddings_batch(texts):
    result = voyage.embed(texts, model="voyage-3-lite")
    return result.embeddings

# Косинусное сходство
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
    result = voyage.embed([question], model="voyage-3-lite")
    question_embedding = result.embeddings[0]
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
            {"role": "system", "content": "Отвечай на основе контекста. Если контекста недостаточно — дополни своими знаниями но скажи об этом."},
            {"role": "user", "content": f"Контекст:\n{context}\n\nВопрос: {question}"}
        ]
    )
    return response.choices[0].message.content

# Запуск
chunks = load_and_split("document.txt")
print(f"Чанков: {len(chunks)}")
print("Создаю embeddings...")

chunk_embeddings = get_embeddings_batch(chunks)  # один запрос для всех чанков
print("Готово\n")

print("Жду 25 секунд перед вопросом...")
time.sleep(25)

question1 = "Как модели запоминают информацию?"
relevant1 = find_relevant(chunks, chunk_embeddings, question1)
context1 = "\n\n".join(relevant1)
print(f"Вопрос: {question1}")
print(f"Ответ: {answer(question1, context1)}\n")