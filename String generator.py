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

def reproduce():
    strings = []
    starter = randomString()
    for i in range(0,101):
        strings.append(starter)
    return strings



#print(randomString())
#print(randomLetters(8))
#print(reproduce())

array = reproduce()
print(array)

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

print(array)
