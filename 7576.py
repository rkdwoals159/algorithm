#토마토~
import sys
from collections import deque
M,N = map(int,input().split())
#map = [list(map(int,input().split())) for _ in range(N)]
map = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ripe = deque()
for i in range(N):
    for j in range(M):
        if map[i][j] == 1:
            ripe.append((i,j)) #세로가로
dir = [(-1,0),(1,0),(0,-1),(0,1)]#상하좌우
while ripe :
    y,x = ripe.popleft() #세로가로
    for i in range(4):
        dx = x+dir[i][1]
        dy = y+dir[i][0]
        
        if 0<=dx<M and 0<=dy<N and map[dy][dx]==0 :
            map[dy][dx] = map[y][x] +1
            ripe.append((dy,dx))


#map_ = sum(map,[])
map_ = [element for array in map for element in array] # 2차원 맵에서 array를 뽑고 그 array에서 element를 뽑음
if map_.count(0) != 0:
    print(-1)
else : print(max(map_)-1)
