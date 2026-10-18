print("------------filter----------------")
num=[55,99,82,47,46,68,91,62,]
result=filter(lambda x:x%2==0,num)
print(list(result))
print("------------filter----------------")
print(                                     )
print(                                     )
fruits=["strawberry","mango","orange","benana","apple","kiwi","berry","painapple"]
l=filter(lambda x: len(x)>5,fruits)
print(list(l))
print(                                     )
print(                                     )
print("------------zip----------------")

students=["Zahra","Setareh","Maede","Donya"]
numbers=[25,29,31,14]
a=zip(students,numbers)
print(list(a))
print(                                     )
print(                                     )
print("------------zip----------------")
name=["Ali","Amir","Reza","Mohammad"]
age=[21,19,32,25]
avrage=[18.75,18.5,19.25,18.25]
for item in zip (name,age,avrage):
    print(item)
print(                                     )
print(                                     )
print("------------zip----------------")
esm=["Ali","Amir","Reza","Mohammad"]
av=[17,18.5,19.5,20]
r=list(filter(lambda x: x[1]>17, zip(esm,av)))
print(r)
print(                                     )
print(                                     )
print("------------zip----------------")
keys=["Name","Last name","Age","Class"]
Value=["Maede","Mohammadzade",17,"Python"]
person=dict(zip(keys,Value))
print(person)
print(                                     )
print(                                     )
print("------------zip----------------")
data=[('Amir', 18.5), ('Reza', 19.5), ('Mohammad', 20)]
vorodi,nomreh=zip(*data)
print(vorodi)
print(nomreh)



