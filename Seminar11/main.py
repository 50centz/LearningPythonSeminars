import random

f = lambda x : random.randint(1, 10)

points = list(map(f, range(1, 10)))

print(f)
print(points)