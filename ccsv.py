import csv
filename = "students.csv"

try:
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        print("نام و نمره دانش‌آموزان:")
        for row in reader:
            name = row['name']
            score = row['score']
            print(f"نام: {name}, نمره: {score}")

except FileNotFoundError:
    print(f"خطا: فایل '{filename}' یافت نشد.")
except Exception as e:
    print(f"خطا در خواندن فایل: {e}")


    
import csv
filename = "students.csv"

with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    print("نام و نمره دانش‌آموزان:")
    for row in reader:
        if float(row['score']) >= 19:
            print(f"نام: {row['name']}, نمره: {row['score']}")
