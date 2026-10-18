import sqlite3

connection=sqlite3.connect("students.db")

cursor=connection.cursor()

#cursor.execute("""
    #CREATE TABLE students(
        #id INTEGER PRIMARY KEY,
        #name TEXT,
        #age INTEGER,
        #course TEXT
#    )
#""")
#connection.commit()
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
connection.commit()

cursor.execute("SELECT * FROM students")
students=cursor.fetchall()

for student in students:
    print(student)
    



