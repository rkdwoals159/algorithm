import sys
N = int(input())

case = [sys.stdin.readline() for _ in range(N)]
cnt = 0
for i in case :
    temp = 0
    case = []

    for j in range(len(i)) :
        if j == 0 : 
            temp = i[j]
            case.append(temp)
        elif i[j] == temp : pass
        elif case.count(i[j]) != 0 : 
            cnt +=1
            break
        else : 
            temp = i[j]
            case.append(temp)
print(N-cnt)



    