N,B = input().split()
B = int(B)
answer = 0
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(N)-1,-1,-1):
    
    if N[i] in alp:
        tmp = alp.index(N[i])+10
        answer += tmp * (B**(len(N)-i-1))
    else: answer += int(N[i]) * (B**(len(N)-i-1))
print(answer)