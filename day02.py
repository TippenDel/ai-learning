import json

# === Aeyrwbb ===
def greet(name, age):
    return f"Привет, {name}! Тебе {age} лет."

def is_adult(age):
    return age >= 18

print(greet("Tippen", 45))
print(is_adult(45))
print(is_adult(15))

# === Функции с default аргументом ===
def create_user(name, age, city="Unknown"):
    return {
        "name": name,
        "age": age,
        "city": city
    }

user1 = create_user("Tippen", 45, "Donetsk")
user2 = create_user("Bob", 30)

print(user1)
print(user2)


# === JSON ===
# Cохранить в файл
users = [user1, user2]

with open("users.json", "w") as f:
    json.dump(users, f, indent=2)

print("Файл сохранен")

# Прочитать из файла
with open("users.json", "r") as f:
    loaded = json.load(f)

print(f"Загружено: {loaded}")
print(f"Первый юзер: {loaded[0]['name']}")

