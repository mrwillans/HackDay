import random
import string

letters = string.ascii_uppercase
target = 'HELLO SAM THIS IS A TEST OF MY CODE'

def randomLetters(length):
    lets = [random.choice(letters) for i in range(0,length)]
    word = ''.join(lets)
    return word

def splitter(target):
    words = target.split()
    ranLettersCount = []
    for i in range(len(words)):
        ranLettersCount.append(len(words[i]))
    return ranLettersCount


def randomString(ranLettersCount):
    ranLet = []
    for i in range(len(ranLettersCount)):
        ranLet.append(randomLetters(ranLettersCount[i]))
    return ' '.join(ranLet)

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
        if score == len(target):
            print('Success!')
            print(array[k])
            return 'success'
        elif score > max:
            max = score
            maxIndex = k
    return maxIndex

starter = splitter(target)
start = randomString(starter)
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


