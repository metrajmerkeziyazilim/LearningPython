import random, math

result = random.random()
result1 = random.random() * 100
result2 = random.uniform(1, 100)
result5 = random.randint(1, 200)
print(result2)

result3 = math.floor(result2)
result4 = math.ceil(result2)


print(result3)
print(result4)
print(result5)
