# Напишите функцию brackets(line), которая определяет, является ли последовательность из круглых скобок правильной. 
from collections import deque
def brackets(line):
    bracket = deque()
    
    for i in line:
        if i in "(":
            
            bracket.append(i)
        elif i in ")" and bracket != deque([]):
            
            bracket.popleft()
        else:
            return False
    return bracket == deque([])
print(brackets("((("))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False