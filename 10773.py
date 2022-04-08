import sys
money = []

N = int(sys.stdin.readline())
for _ in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0 : 
        money.pop()
    else : money.append(tmp)
    
print(sum(money))