from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.request import HTTPXRequest
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

histories = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    await update.message.reply_text("Привет! Я AI ассистент. Задай любой вопрос.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    if user_id not in histories:
        histories[user_id] = [
            {"role": "system", "content": "Ты полезный AI ассистент. Отвечай коротко и по делу."}
        ]
    
    histories[user_id].append({"role": "user", "content": text})
    
    response = client.chat.completions.create(
        model="kr/claude-haiku-4.5",
        messages=histories[user_id]
    )
    
    answer = response.choices[0].message.content
    histories[user_id].append({"role": "assistant", "content": answer})
    
    await update.message.reply_text(answer)

request = HTTPXRequest(connect_timeout=30, read_timeout=30)
app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).request(request).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен...")
app.run_polling()
