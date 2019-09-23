def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

    # Driver Program


i=1
sum=0
while Fibonacci(i) < 4000000:
    #print(Fibonacci(i))
    if(Fibonacci(i) % 2 == 0):
        sum = sum + Fibonacci(i)
        #print(sum)
    i = i + 1

print(sum)