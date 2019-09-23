nums = range(1,101)
sum1 = 0
sum2 = 0

for i in nums:
    square = i*i
    sum1 = sum1 + square
    sum2 = sum2 + i

fin = sum2*sum2

print(sum1)
print(fin)
print(-sum1+fin)