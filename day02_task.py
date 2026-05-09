import json

def add_skill(user, skill):
    user["skills"].append(skill)
    return user

def filter_adults(users):
    return [user for user in users if user["age"] >= 18]

users = [
    {
        "name": "Alice", 
        "age": 30, 
        "skills": ["Python"]
    },
    {
        "name": "Bob",
        "age": 17, 
        "skills": ["JavaScript"]
    },
    {
        "name": "Charlie", 
        "age": 25, 
        "skills": ["Java"]
    },
]

add_skill(users[0], "Django")
add_skill(users[1], "React")

adults = filter_adults(users)

with open("result.json", "w") as f:
    json.dump(adults, f, indent=2)

print("Файл сохранен")

with open("result.json", "r") as f:
    loaded = json.load(f)

print(f"Загружено: {loaded}")

for user in loaded:
    print(f"User: {user['name']}")