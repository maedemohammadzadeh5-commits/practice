#numbers=[1,2,5,4,8,9,6]
#def  is_even(numbers):
#    return numbers%2==0
#result=filter(is_even,numbers)
#print(list(result))



#numbers=[-8,5,0,11,-15]
#result=filter(lambda x:x>3,numbers)
#print(list(result))

#names=["","hi","","maede",0,None]
#result=filter(None,names)
#print(list(result))

#num=[-5,5,8,-122,45]
#positiv=filter(lambda x: x>0 , num)
#print(list(positiv))



studentd=[(14,"ali"),(11,"amir"),(20,"maede"),(16,"setare")]
passed=filter(lambda x:x[0]>=10,studentd)
print(list(passed))


