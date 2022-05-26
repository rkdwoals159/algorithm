from collections import deque
import sys
sys.setrecursionlimit(10**6)

T = int(input())
T_C = deque([])
for _ in range(T):
    T_C.append(list(map(int,input().split())))
    K = T_C[-1][2]
    case = []
    for _ in range(K):
        case.append(list(map(int,input().split())))
    T_C.append(case)


for _ in range(T):
    M,N,K = T_C.popleft()
    case = T_C.popleft()
    area = [[0]*M for _ in range(N)]
    for a,b in case: area[b][a] = 1
    dir_ = [(-1,0),(0,1),(1,0),(0,-1)]

    max_num = 2
    def dfs(x,y):
        global max_num
        for i in dir_:
            dx = x + i[0]
            dy = y + i[1]

            if 0<=dx <M and 0<=dy<N:
                if area[dy][dx] ==1:
                    area[dy][dx] = max_num
                    dfs(dx,dy)
    for x,y in case:
        if area[y][x] != 0: 
            dfs(x,y)
            max_num +=1
            

    # for i in range(N):
    #     for j in range(M):
    #         print(area[i][j],end=' ')
    #     print()
    # print()

    area = [y for x in area for y in x]
    # print(area)
    # print(max(area))
    answer = area.count(1)
    area = list(set(area))
    answer += len(area)-1
    if 1 in area : answer -=1
    print(answer)



