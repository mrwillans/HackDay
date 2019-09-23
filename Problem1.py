import numpy as np

numbers = range(1,1001)

sum = 0

i=3

for i in numbers:
    if ((i % 3 == 0) or (i % 5 == 0)):
        sum = sum + i


print(sum)

