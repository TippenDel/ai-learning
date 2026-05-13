from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

def load_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def split_chunks(text, chunk_size=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def find_relevant(chunks, question):
    question_words = set(question.lower().split())
    scored = []

    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(question_words & chunk_words)
        scored.append((score, chunk))
    scored.sort(reverse=True)
    return [chunk for score, chunk in scored]

def answer(question, context):
    response = client.chat.completions.create(
        model="kr/claude-haiku-4.5",
        messages=[
            {"role": "system", "content": "Отвечай только на основе предоставленного контекста."},
            {"role": "user", "content": f"Контекст:\n{context}\n\nВопрос: {question}"}
        ]
    )
    return response.choices[0].message.content

text = load_document('document.txt')
chunks = split_chunks(text)
question = "Что такое RAG?"
relevant = find_relevant(chunks, question)
context = "\n\n".join(relevant)
print(answer(question, context))