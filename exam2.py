maximum = lambda a, b: a if a > b else b
result = maximum(10, 25)
print(result)

#2

ages = [10, 15, 20, 30, 40]
new_ages = list(map(lambda age: age + 1, ages))
print(new_ages)

