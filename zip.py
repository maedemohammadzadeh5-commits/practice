student=["Ali","Zahra","Fateme","Maede"]
age=[23,29,17,15]
score=[19,20,19,20]
for item in zip(student,age,score):
    print(item)

#student=["Ali","Zahra","Fateme","Maede"]
#age=[23,29,17,15]
#result=zip(student,age)
#print(list(result))

#keys=["name","age","score"]
#value=["Ali","18","19.5"]
#person=dict(zip(keys,value))
#print(person)

#names=["maede","setare","arsam","hasti"]
#scores=[18.75,20,19.25,18]
#for names,scores in zip(names,scores):
#    print(names,scores)


#unzip
#p=[("maede",18),("setare",16),("arsam",12),("hasti,20")]
#name,sc=zip(*p)
#print(name)
#print(sc)
#*=unzip


#colors=["red","black","white","green"]
#scores=[18.75,20,19.25,18]
#some=zip(colors,scores)
#resul=filter(lambda some: some[1]>10,some)
#print(list(resul))










