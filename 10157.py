N,M = map(int, input().split())
num = int(input())
n = N
m = M
case = [1,0]
dir_ = 0 # 0: 북 ,1: 동, 2: 남 , 3: 서
for i in range(num):
    if dir_ == 0: #북쪽방향 진행이면
        if case[1] != m :
            case[1] += 1
        else : 
            case[0] += 1
            dir_ == 1
            
    elif dir_ == 1: #동쪽방향이면
        if case[1] != n :
            case[0] +=1
        else :
            case[1] -=1 
            dir_ == 1
    elif dir_ == 2: #남쪽방향이면
        if case[1] != M-m+1 :
            case[1] -=1
        else : 
            case[0] -=1
            dir_ == 1
    else : #서쪽방향이면
        if case[1] != N-n+1 :
            case[0] -=1
        else :
            case[1] -=1 
            dir_ == 1
    
print(case[0],case[1])