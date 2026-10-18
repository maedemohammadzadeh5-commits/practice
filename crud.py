import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()
cursor.execute("DELETE FROM students")




cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        course TEXT
    )
""")

cursor.execute("SELECT COUNT(*) FROM students")

cursor.execute("INSERT INTO students(name,age,course) VALUES(?,?,?)", ("Ali", 22, "python"))
cursor.execute("INSERT INTO students(name,age,course) VALUES(?,?,?)", ("Sara", 25, "art"))
cursor.execute("INSERT INTO students(name,age,course) VALUES(?,?,?)", ("Setare", 21, "music"))
cursor.execute("INSERT INTO students(name,age,course) VALUES(?,?,?)", ("Maede", 23, "python"))
cursor.execute("INSERT INTO students(name,age,course) VALUES(?,?,?)", ("Reza", 18, "game"))
cursor.execute("INSERT INTO students(name,age,course) VALUES(?,?,?)", ("Arsam", 29, "game"))
connection.commit()

print("-------------")
cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)
print("-------------")
#connection.close()



print("----------found------------")
cursor.execute("""
SELECT * FROM students
WHERE name=?
""",("Sara",))
students=cursor.fetchone()
print(students)

print("----------found------------")
students_id=2

cursor.execute("""
               SELECT *FROM students
               WHERE id=?
               """,(students_id,))
student=cursor.fetchone()
print(student)



cursor.execute("""
               UPDATE students
               SET age=?
               WHERE id=?
               """,(28,3))
connection.commit()

students_id=3

cursor.execute("""
               SELECT *FROM students
               WHERE id=?
               """,(students_id,))
student=cursor.fetchone()
print(student)


cursor.execute("""
DELETE FROM students
WHERE id=?
""",(1,))
connection.commit()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)





















