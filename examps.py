# برنامه‌ای بنویسید که این سری را به‌صورت بازگشتی تولید کند.
def fibonacci(x):
    if x<=1:
        return x
    return fibonacci(x-1)+fibonacci(x-2)
x=10
print([fibonacci(i)for i in range(x)])
 
print("--------------ضرب-----------------")


a=float(input("Enter first number : "))
b=float(input("Enter second number: "))

print(f" sum: {a+b}")
print(f" product {a*b}")

print("-------------چاپ مجموع عدد قبلی  و فعلی -------------")

ab=[1,2,3,4,5,6,7,8,9,10]
for i in range(1,len(ab)):
    print(ab[i]+ab[i-1])

print("-------------حذف کاراکتر از ابتدای رشته-------------")

text=input("Enter string : ")
n=int(input("Enter number to remove : "))
print(text[n:])

print("-----------شمارش رشته‌های تکراری---------")

items=["apple", "banana", "apple", "orange", "banana", "apple"]
counts={}

for item in items:
    counts[item]=counts.get(item,0)+1
dup={k:v for k,v in counts.items() if v>1}
print(dup)



print("--------------افرودن اعداد زوج به لیست --------------")

a=int(input("Enter your number : "))
b=[]
if a %2==0:
    b.append(a)
    print(b)
else:
    print("number is not correct")



