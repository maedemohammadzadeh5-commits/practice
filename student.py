student=["Ali","Amir","zahra"]

try:
    s1=int(input("enter student number:"))
    print(f"name:{student[s1]}")

except IndexError:
    print("کاربر در لیست وجود ندارد")
except ValueError:
    print("Enter number")


