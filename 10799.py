import sys
case = sys.stdin.readline().rstrip()

stack = 0
lazer = False
answer = 0
for i in case:
    if i == '(' :
        stack +=1
        lazer = True
    else : 
        if lazer == True : 
            stack -=1
            answer += stack 
            lazer = False
        else : 
            answer +=1
            stack -=1
print(answer)