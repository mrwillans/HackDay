x = range(100,999)
y = range(100,999)
pals = []
for i in x:
    for j in y:
        num = i*j
        if (str(num)==str(num)[::-1]):
            pals.append(num)

print(pals[-1])

