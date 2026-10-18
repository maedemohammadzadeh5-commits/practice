import json

student={
     "name": "Ali",
    "age": 18,
    "score": 19
}

json_data=json.dumps(student)
print(json_data)