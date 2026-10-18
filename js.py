import json


with open("students.json","r",encoding="utf-8")as file:
    students=json.load(file)

for student in students:
      print(student["name"],student["score"])










