#def zoj_fard(a):
#    if a%2==0:
#        return("number=zoj")
#    else:
 #       return("number=fard")
    
print(f"number : {zoj_fard(int(input("enter number")))}")

zoj= lambda x:"zoj" if x%2==0 else "fard"
x=int(input("ENTER NUMBER PLEAS:"))
print(zoj(x))


t=lambda age:"child" if age <12 else "tenage" if age < 18 else "adult"
age=int(input("enter your age :"))
print(t(age))



