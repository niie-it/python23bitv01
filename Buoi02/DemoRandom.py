from random import *

print(sample(range(1, 46), 3))


arr = []
while len(arr) < 6:
    num = randint(1, 45)
    if num not in arr:
        arr.append(num)
      
# print(sorted(arr))
# print(arr)