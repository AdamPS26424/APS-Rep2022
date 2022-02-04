#Language: Python
import readchar
import string
import numpy as np

# 1. convertion hours (3600), minutes (60), seconds to total seconds
hour = 0
minute = 0
second = 0
hour = input('Enter Hour: ')
minute = input('Enter Minute: ')
second = input('Enter Seconds: ')
totalseconds = (int(hour) * 3600) + (int(minute) * 60) + (int(second))
print("total time: " + str(totalseconds) + " seconds")

# 2. recursive factorial
value = 1
value = input('Enter Factorial: ')
value = int(value)
factorVal = 1
for I in range(value):
    factorVal = factorVal * (I + 1)
print('Decimal value: ' + str(factorVal))

# 3. leap year checker
year = 1
year = input('Enter year value: ')
year = int(year)
if (year % 4 == 0):
    print(str(year) + ' is a Leap Year')
else:
    print(str(year) + ' is not a Leap Year')

# 4. Palindrome Checker
word = ''
word = input('Entry Word: ')
word = word.lower().replace(' ', '')
if (word == word[::-1]):
    print(word + ' is palindrome')
else:
    print(word + ' is not palindrome')

# 5. WordChecker but only used values to print
Dword = ''
Dword = input('Entry Word: ')
Dword = Dword.lower().replace(' ', '')
Dlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']
DlistVal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in Dword:
    if (Dword.__contains__(i)):
        for ind, j in enumerate(Dlist):
            if (i == j):
                DlistVal[ind] += 1
                break
for ind, j in enumerate(DlistVal):
    if j > 0:
        print(str(Dlist[ind]) + "     " + str(j))
print('total used words: ' + str(sum(DlistVal)))

# 6 Pascal Triangle Creator
PascalLen = 0
PascalLen = input('Pascal length: ')
PascalLen = int(PascalLen)
'''
1
11
121
1331
14641
dst
'''
if (PascalLen >= 1):
    Drow = [1]
    y = [0]
    for x in range(PascalLen):
        print(Drow)
        Drow = [left + right for left, right in zip(Drow + y, y + Drow)]

# 7 Removes all special characters (includes space)
DSentence = ''
DSentence = input('Sentence display: ')
newDSentence = ''
for i in DSentence:
    if (i.isalnum()):
        newDSentence += i
print('new Sentence Result: \n' + newDSentence)

print("Test Finished...\nPress any key to exit...")
k = readchar.readchar()
exit()