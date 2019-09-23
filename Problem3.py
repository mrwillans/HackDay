import numpy as np

check_me = range(100000, int(np.sqrt(600851475143)))

primes = []
for i in check_me:
    for j in range(2, i):
        if not i % j:
            break
    else:
        primes.append(i)
sum = []
for i in primes:
    if 600851475143 % i == 0:
        sum.append(i)

print(sum[-1])

