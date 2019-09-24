import random
import string

letters = string.ascii_uppercase
target = 'METHINKS IT IS LIKE A WEASEL'

def randomLetters(length):
    lets = [random.choice(letters) for i in range(0,length)]
    word = ''.join(lets)
    return word

def randomString():
    return ' '.join([randomLetters(8),randomLetters(2),randomLetters(2),randomLetters(4),randomLetters(1),randomLetters(6)])

def reproduce(input):
    strings = []
    starter = input
    for i in range(0,101):
        strings.append(starter)
    return strings



#print(randomString())
#print(randomLetters(8))
#print(reproduce())

#array = reproduce()

#print(array)

def mutator(array):
    for i in range(len(array)):
        row = array[i]
        #print(row)
        for j in range(len(row)):
            #print(j)
            if random.randint(0,100) < 5 and row[j] != ' ':
                #i.replace(i[j], random.choice(letters),1)
                row = row[:j] + random.choice(letters) + row[j + 1:]
                #i[j] = random.choice(letters)
        #print(row)
        array[i] = row
    return array

def checker(array):
    max = 0
    maxIndex = 0
    for k in range(len(array)):
        score = 0
        check = array[k]
        for l in range(len(check)):
            if check[l] == target[l]:
                score +=1
        if score == 28:
            print('Success!')
            print(array[k])
            return 'success'
        elif score > max:
            max = score
            maxIndex = k
    return maxIndex

start = randomString()
initialArray = reproduce(start)
mutated = mutator(initialArray)
nextIndex = checker(mutated)
nextArray = mutated[nextIndex]
while True:
    initialArray = reproduce(nextArray)
    mutated = mutator(initialArray)
    nextIndex = checker(mutated)
    if nextIndex=='success':
        break
    nextArray = mutated[nextIndex]
    print(nextArray)
