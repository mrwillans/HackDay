div = range(1, 21)

test = range(20, 1000000000, 20)

for j in test:
    nums = []
    for i in div:
        if (j % i == 0):
            nums.append(i)
            #print(nums)
    if (len(nums) == 20):
        print(j)
        break

