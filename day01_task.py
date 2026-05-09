person = {
    "name": "Tippen",
    "age": 45,
    "city": "Donetsk",
    "skills": ["Python", "Git", "AI"]
}

for key, value in person.items():
    print(f"{key}: {value}")

person["skills"].append("LLM")
print(f"Added skill: {person['skills']}")

print(f"Total skills: {len(person['skills'])}")