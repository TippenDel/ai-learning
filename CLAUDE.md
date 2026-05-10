# AI Learning Roadmap — Personal Context

## Студент
- Учил JS 4 года назад (RS School), надо вспоминать
- Python: нулевой уровень, начали с нуля
- Время: 3–4 часа в день
- Цель: фриланс через 3–4 месяца + свой AI стартап
- ОС: macOS
- Бюджет: максимально бесплатно

## Среда
- Python 3.13.5 ✅
- Git 2.15.0 ✅
- VS Code ✅
- .venv — виртуальное окружение в папке проекта ✅
- Poetry: не нужен, используем venv/pip

## GitHub
https://github.com/TippenDel/ai-learning

## API и сервисы
- OmniRoute: base_url=http://localhost:20128/v1, модель=kr/claude-haiku-4.5
- Voyage AI: embeddings (VOYAGE_API_KEY в .env), модель=voyage-3-lite, лимит 3 RPM без карты
- Groq: подключён в OmniRoute но embeddings не поддерживает
- Telegram бот: t.me/MyFirstBotAI26_bot

## Текущий статус — что сделано

| Файл | Что изучили |
|------|-------------|
| basics.py | переменные, списки, словари, циклы, классы |
| functions_json.py | функции, JSON, фильтрация данных |
| ai_api.py | AI API через OmniRoute/Kiro, dotenv, system prompt |
| chat_console.py | консольный чат, история через messages[], while loop |
| fastapi_server.py | FastAPI сервер, декораторы, Swagger UI, curl |
| fastapi_history.py | история чата в API, DELETE/GET /history |
| telegram_bot.py | Telegram бот, история на пользователя, polling |
| rag.py | RAG с нуля, чанки, keyword поиск, ответ по контексту |
| rag_voyage.py | RAG с embedding поиском, косинусное сходство, Voyage AI |

## Следующий шаг
- Подключить RAG к Telegram боту — реальный продукт
- Потом: Docker + деплой

## Важные концепции (уже понял)
- messages[] — история диалога, отправляется целиком каждый раз
- histories{} — словарь user_id → история для мультипользовательского чата
- @app.post("/chat") — декоратор регистрирует функцию как обработчик маршрута
- chunks — размер влияет на точность поиска vs контекст
- keyword поиск — ищет слова, не понимает смысл
- embedding поиск — ищет по смыслу, работает когда слова разные но смысл одинаковый
- cosine similarity — мера близости двух векторов (от -1 до 1)
- grounding — модель отвечает только на основе контекста, не выдумывает

---

## Roadmap (4 фазы)

### Фаза 1 — Фундамент (выполнено за 1 неделю) ✅
- Python basics
- AI API
- FastAPI
- Telegram бот
- RAG с нуля

### Фаза 2 — LLM Engineering (текущая)
- RAG с embeddings ✅
- Подключить RAG к Telegram боту
- Docker + деплой на Railway/Render
- AI Agents basics
- PostgreSQL + pgvector

Проект: AI-ассистент для бизнеса — загружаешь доки компании, бот отвечает клиентам.

### Фаза 3 — Стек для фриланса (месяц 3–4)
- Redis + очереди
- AI Agents (LangGraph)
- Streamlit / Gradio
- n8n / Make — AI автоматизация

### Фаза 4 — Стартап (месяц 5–12)
- Fine-tuning (LoRA, QLoRA)
- Open-source модели через Ollama
- Scalable architecture

---

## Правила обучения
- Код пишем руками, не копируем
- Каждый проект публично на GitHub
- Вопросы по пониманию задаются по ходу

## JS → Python шпаргалка

| JS | Python |
|----|--------|
| let x = 5 | x = 5 |
| arr.map(f) | [f(x) for x in arr] |
| arr.filter(f) | [x for x in arr if f(x)] |
| JSON.parse() | json.loads() |
| JSON.stringify() | json.dumps() |
| Promise.all() | asyncio.gather() |
| try/catch | try/except |
| null/undefined | None |

## Реальные ставки (Eastern Europe, 2026)
- Начало (3–4 мес): $30–50/час
- Junior (6–9 мес): $50–80/час
- Middle (1–2 года): $80–120/час