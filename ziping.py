students=["Ali","Sara","Maede","Setare","Mehrane"]
numbers=[12,23,45,78,47]
result=zip(students,numbers)
print(list(result))

print("                                      ")
print("                                       ")

esm=["Ali","Sara","Maede"]
age=[21,20,18]
grade=[16.5,17.32,19.89]
for item  in zip(esm,age,grade):
    print(item)


print("                                      ")
print("                                       ")



s=["Ali","Sara","Maede"]
avrage=[16.5,17.32,19.89]
res=zip(s,avrage)
some=filter(lambda x: x[1]>17 ,res)
print(list(some))

print("                                      ")
print("                                       ")


keys=["name","age","avrage"]
Value=["Maede","17","19.89"]
person=dict(zip(keys,Value))
print(person)



print("                                      ")
print("                                       ")


un=[("maede",18),("setare",16),("arsam",12),("hasti,20")]
players,scores=zip(*un)
print(players)
print(scores)

