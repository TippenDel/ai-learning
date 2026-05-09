# AI Learning Roadmap — Personal Context

## Студент
- Учил JS 4 года назад (RS School), надо вспоминать
- Python: нулевой уровень, начинаем с нуля
- Время: 3–4 часа в день
- Цель: фриланс через 3–4 месяца + свой AI стартап
- ОС: macOS
- Бюджет: максимально бесплатно

## Среда
- Python 3.13.5 ✅
- Git 2.15.0 ✅
- VS Code ✅
- Poetry: НЕ устанавливали (отложили, пока не нужен)

## GitHub
https://github.com/TippenDel/ai-learning

## Текущий статус
- День 1 ✅ — переменные, списки, словари, циклы, классы
- День 2 ✅ — функции, JSON, фильтрация данных
- День 3 ✅ — AI API через OmniRoute/Kiro, dotenv, system prompt
- День 4 — следующий (консольный чат с историей диалога)
- Git настроен, код на GitHub запушен
- OmniRoute: base_url=http://localhost:20128/v1, модель=kr/claude-haiku-4.5

---

## Roadmap (4 фазы)

### Фаза 1 — Фундамент (месяц 1–2)
**Цель:** писать рабочий Python код + вызывать LLM API

- Неделя 1–2: Python basics (переменные, функции, классы, циклы, словари, списки, исключения, файлы, json, requests)
- Неделя 3–4: OpenAI/Anthropic API + FastAPI + деплой на Railway/Render

**Проект:** Телеграм-бот с GPT-4o, отвечает на вопросы по PDF. Живой деплой.

### Фаза 2 — LLM Engineering (месяц 2–3)
**Цель:** строить реальные AI продукты, первые заказы

- RAG (Retrieval-Augmented Generation)
- Vector DB: Chroma → Pinecone
- LangChain / LlamaIndex
- Prompt Engineering (system prompts, few-shot, chain-of-thought)
- Embeddings
- PostgreSQL + pgvector
- Docker (сдвинут сюда из фазы 3)
- AI Agents basics (сдвинут сюда — высокий спрос)

**Проект:** AI-ассистент для бизнеса — загружаешь доки компании, бот отвечает клиентам. Это продаётся.

### Фаза 3 — Стек для фриланса (месяц 3–4)
**Цель:** брать заказы от $500+

- Redis + очереди (Celery/ARQ)
- AI Agents продвинутый уровень (LangGraph)
- Streamlit / Gradio — быстрые UI
- n8n / Make — AI автоматизация (продаётся дорого)

**Проект:** AI automation для бизнеса — парсит письма, классифицирует, отвечает, логирует в Google Sheets.

### Фаза 4 — Стартап + экспертиза (месяц 5–12)
- Fine-tuning (LoRA, QLoRA)
- Open-source модели: Llama, Mistral, Qwen через Ollama/vLLM
- Scalable architecture
- AI Product thinking

---

## План по дням — Неделя 1

| День | Тема | Файл |
|------|------|------|
| 1 | Переменные, списки, словари, циклы, условия, классы | day01.py |
| 2 | Функции, исключения, работа с файлами, json | day02.py |
| 3 | requests — делаем запрос к OpenAI API вручную | day03.py |
| 4 | Git: init, add, commit, push. Проект на GitHub | — |
| 5–6 | FastAPI: первый эндпоинт, POST запрос | day05.py |
| 7 | Деплой на Railway. Живой URL | — |

---

## Правила обучения
- Код пишем руками, не копируем
- Каждый проект публично на GitHub
- Ошибки присылать мне — разбираем
- Без курсов, без книг — только практика + я
- Poetry не нужен сейчас, используем стандартный venv/pip

## JS → Python шпаргалка

| JS | Python |
|----|--------|
| `let x = 5` | `x = 5` |
| `const arr = []` | `arr = []` |
| `arr.map(f)` | `[f(x) for x in arr]` |
| `arr.filter(f)` | `[x for x in arr if f(x)]` |
| `obj.key` | `obj["key"]` |
| `JSON.parse()` | `json.loads()` |
| `JSON.stringify()` | `json.dumps()` |
| `Promise.all()` | `asyncio.gather()` |
| `try/catch` | `try/except` |
| `null/undefined` | `None` |
| `===` | `==` (или `is` для None) |
| `&&` | `and` |
| `\|\|` | `or` |
| `!` | `not` |

## Реальные ставки (Eastern Europe, 2026)
- Начало (3–4 мес): $30–50/час
- Junior (6–9 мес): $50–80/час
- Middle (1–2 года): $80–120/час

## Топ навыков по спросу 2026
1. AI Integration / Chatbot development (+71–178% на Upwork)
2. RAG системы — 80% реального фриланса
3. AI Agents — премиум +15–20% к ставке
4. Docker + деплой — обязательно
5. Prompt Engineering — entry point

## Способы заработка
- **0–3 мес:** AI automation для бизнеса, простые боты
- **3–6 мес:** RAG для конкретных ниш, B2B AI решения
- **6–12 мес:** AI SaaS, агентство, стартап

## Что НЕ нужно сейчас
- Poetry (добавим в фазе 2)
- Математика/теория ML (не нужна для фриланса)
- TensorFlow (устарел, только PyTorch)
- Академические курсы
- LangChain до понимания RAG вручную