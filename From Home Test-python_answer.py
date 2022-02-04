#Long story short: American's 24 Game
'''
 The American's 24 Game

 This is a game where you get four numbers (in this case, from 1 to 9) that are randomly selected,
 and try to combine them (using the four basic operations +, -, *, and /) to make the number 24.
 The rules are simple, you must use all four numbers and only those four numbers, and they can only 
 be used once each.

 Given any four digits in the range 1 to 9, which may have repetitions,
 Using just the +, -, *, and / operators and the possible use of brackets, (), 
 to show any combination with an answer of 24.

 Note: you cannot form multiple digit numbers from the supplied digits,
 so an answer of 12+12 when given 1, 2, 2, and 1 would not be allowed.
'''

import string
import math
import itertools
from itertools import permutations,combinations_with_replacement
from itertools import product
import re
#import readchar as readchar

def groupPatterns(count,pattern=None):
    arr = pattern or "X"*count
    if len(arr) < 2 : return [arr]
    result = []
    for mid in range(1,len(arr)):
        leftPattern  = groupPatterns(count,arr[:mid])
        rightPattern = groupPatterns(count,arr[mid:])
        for left,right in product(leftPattern,rightPattern):
            result += [left + right]
            if len(left)  > 1 : result += ["(" + left + ")" + right]
            if len(right) > 1 : result += [left + "(" + right + ")"]
            if len(left) > 1 and len(right) > 1:
                result += ["(" + left + ")(" + right + ")"]
    if pattern: return result # recursion
    patterns = []
    for pat in sorted(set(result),key=lambda x:len(x)):
        pat = re.sub("X(?=X)", r"X+",  pat)  # XX --> X+X
        pat = re.sub("X\(",    r"X+(", pat)  # X( --> X+(
        pat = re.sub("\)X",    r")+X", pat)  # )X --> )+X
        pat = re.sub("\)\(",   r")+(", pat)  # )( --> )+(
        patterns.append(pat)
    return patterns

numbers = ["0","0","0","0"]
inputs = 0
while inputs < 4:
    value = input("Please enter your value: ")
    if (value.isnumeric()):
        if (int(value) <= 9 and int(value) > 0):
            numbers[inputs] = value
            inputs += 1
            print("value of:"+value+" is accepted\n")
        else:
            print("value is not a positive single digit integer...\n")
    else:
        print("value is NOT an integer...\n")
print("Inserted values are: ", numbers, sep=", ")
print("\nWith target to play the 24 Game...\n")
target = 24
operators = ["+","-","*","/"]
groups = groupPatterns(len(numbers))
foundTarget = False
foundTargets = 0
seen = set()
for values in permutations(numbers,len(numbers)):
    for operCmb in combinations_with_replacement(operators,len(numbers)-1):
        for oper in permutations(operCmb,len(numbers)-1):
            formulaKey = "".join(oper+values)
            if formulaKey in seen: continue # ignore variations on parentheses alone
            for pattern in groups:
                formula = "".join(o+p for o,p in zip([""]+list(oper), pattern.split("+")))
                formula = "".join(v+p for v,p in zip([""]+list(values),formula.split("X")))
                try:
                    if eval(formula) == target:
                        print(formula,"=",target)
                        seen.add(formulaKey)
                        if (not foundTarget):
                            foundTarget = True
                        foundTargets += 1
                        break
                except:
                    pass
if (not foundTarget):
    print("no combination is possible to reach The 24\n")
else:
    print("possible combination(s) of "+str(foundTargets)+" that capable of reaching The 24 has been printed\n")
    
#print("Press any keys to exit")
#import readchar as readchar