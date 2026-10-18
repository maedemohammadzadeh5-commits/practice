a=float(input("enter math score :"))
b=float(input("enter art score :"))
c=float(input("enter scienes score :"))
n=[a,b,c]
avg= lambda n: sum (n)/len(n)
a = avg(n)

s=lambda x: "bitchin" if x>18 else "good" if 16<x<18 else "challenging" if 14<x<16 else "reject"
print(s(a))




