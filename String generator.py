import random
import string

letters = string.ascii_uppercase

def randomLetters(length):
    lets = [random.choice(letters) for i in range(0,length+1)]
    word = ''.join(lets)
    return word

def randomString():
    return ' '.join([randomLetters(8),randomLetters(2),randomLetters(2),randomLetters(4),randomLetters(1),randomLetters(6)])

#print(randomString())
#print(randomLetters(8))