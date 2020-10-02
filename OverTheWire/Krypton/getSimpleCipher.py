#!/usr/bin/python3

import sys

## Getting frequency files
singleLetterPath = '/home/slop/Documents/misc/singleLetterFreq.txt'
twoLetterPath    = '/home/slop/Documents/misc/twoLetterFreq.txt'
threeLetterPath  = '/home/slop/Documents/misc/threeLetterFreq.txt'
singleLetterList = open(singleLetterPath, 'r').read(-1).split('\n')[:-1]
twoLetterList    = open(twoLetterPath, 'r').read(-1).split('\n')[:-1]
threeLetterList  = open(threeLetterPath, 'r').read(-1).split('\n')[:-1]


## Loading files into a single string
totalString = str(sys.stdin.read())
totalString = totalString.replace(' ', '')

# Finding single and three letter frequency
singleLetterFreq = {}
twoLetterFreq    = {}
threeLetterFreq  = {}

for i, letter in enumerate(totalString):
    if letter not in singleLetterFreq.keys():
        singleLetterFreq[letter] = 1

    else:
        singleLetterFreq[letter] += 1

    if i < len(totalString) - 3:
        if totalString[i:i+3] not in threeLetterFreq.keys():
            threeLetterFreq[totalString[i:i+3]] = 1

        else:
            threeLetterFreq[totalString[i:i+3]] += 1

    if i < len(totalString) - 2:
        if totalString[i:i+2] not in twoLetterFreq.keys():
            twoLetterFreq[totalString[i:i+2]] = 1

        else:
            twoLetterFreq[totalString[i:i+2]] += 1

singleLetterFreq = sorted(singleLetterFreq.items(), key=lambda x: x[1], reverse=True)
twoLetterFreq    = sorted(twoLetterFreq.items(), key=lambda x: x[1], reverse=True)
threeLetterFreq  = sorted(threeLetterFreq.items(), key=lambda x: x[1], reverse=True)


print(singleLetterList)
print(singleLetterFreq[:26])
print()
print(twoLetterList)
print(twoLetterFreq)
print()
print(threeLetterList)
print(threeLetterFreq[:26])


## FOR SURE
# J -> T
# D -> H
# S -> E
# N -> R
# U -> D

# Q -> O
# W/G -> N
# G -> F
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#            A    A    A    A    |    A    A    |    A    A    A    A    A    A    A    A    A    |    A    |    A    A    A    A    A    A
#            |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
cipher   = [' ', 'A', 'C', 'U', 'S', 'F', ' ', 'D', 'I', ' ', 'K', 'L', ' ', 'G', 'Q', 'P', ' ', 'N', ' ', 'J', 'M', 'V', 'W', 'X', 'Y', 'Z']

output = ''
for letter in totalString:
    if letter != '\n':
        try:
            output += alphabet[cipher.index(letter)]
        except:
            output += ' '

print(totalString)
print(output)
