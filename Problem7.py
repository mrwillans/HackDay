check_me = range(1,105000,2)

primes = []
for i in check_me:
    for j in range(2, i):
        if not i % j:
            break
    else:
        primes.append(i)

print(primes[10000])