name = "Tippen"
age = 45
skills = ["Python", "Git", "AI", "LLM", "Docker"]
goal = "AI Engineer"

print(f"Привет, {name}!")
print(f"Навыки: {skills}")
print(f"Цель: {goal}")

skills.append("FastAPI")
print(f"Добавил: {skills}")

person = {
    "name": "Tippen",
    "city": "Donetsk",
}

print(f"Город: {person['city']}")

for skill in skills:
    print(f"Учу: {skill}")

if age >= 18:
    print("Взрослый разработчик")   