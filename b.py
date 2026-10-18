import sqlite3


connection=sqlite3.connect("students.db")
cursor=connection.cursor()

cursor.execute("""
    INSERT INTO students(name,age,course)
    VALUES(?,?,?)
""",("Ali",22,"python"))


cursor.execute("""
    INSERT INTO students(name,age,course)
    VALUES(?,?,?)
""",("Sara",25,"art"))


cursor.execute("""
    INSERT INTO students(name,age,course)
    VALUES(?,?,?)
""",("Setare",21,"music"))
cursor=connection.commit()

cursor.execute("SELECT * FROM students")
students=cursor.fetchall()

for student in students:
    print(student)

connection.close()
