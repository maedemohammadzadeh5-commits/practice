temps=[0,20,25,35,40]
def to_fahrenheit(c):
    return (c*9/5)+32
result=list(map(to_fahrenheit,temps))
print(result)