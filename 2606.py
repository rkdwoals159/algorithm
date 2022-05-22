#-----------------dfs----------------------
N = int(input())
M = int(input())
case = [list(map(int,input().split())) for _ in range(M)]
visited = [0] * (N+1)
answer = 0
def dfs(i):
    global answer
    if visited[i] == 1:
        return
    else:
        answer +=1
        visited[i] = 1
        for j in case:
                if j[0] == i:
                    dfs(j[1])
                elif j[1] == i:
                    dfs(j[0])
dfs(1)
print(answer-1)



#-----------------bfs----------------------
from collections import deque
N = int(input())
M = int(input())
case = [list(map(int,input().split())) for _ in range(M)]
visited = [0] * (N+1)
bfs = deque([1])
answer = 0
while bfs:
    idx = bfs.popleft()
    if visited[idx] == 1:
        continue
    else: visited[idx] = 1 
    answer +=1
    for i in case:
        if i[0] == idx :
            bfs.append(i[1])
        elif i[1] == idx:
            bfs.append(i[0])
print(answer-1)

