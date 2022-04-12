# 벽 부수고 이동하기
 
# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 
# 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 
# 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

# 출력
# 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

# 예제 입력 1 
# 6 5
# 00000
# 11110
# 10010
# 00000
# 01111
# 00000
# 예제 출력 1 
# 15
# 예제 입력 2 
# 4 4
# 0111
# 1111
# 1111
# 1110
# 예제 출력 2 
# -1
from collections import deque

dx = [0,-1, 0, 1]
dy = [-1,0,1,0]
def bfs():
    visit = [[[0]*2  for _ in range(M)] for _ in range(N)]
    visit[0][0][0] = 1
    while q:
        x,y,wall = q.popleft()
        if x==(N-1) and y==(M-1): 
            return visit[x][y][wall] #맨 끝 도달할 경우 종료
        for i in range(4) : #상하좌우 반복
            if 0<= x+dx[i]<N and 0<=y+dy[i]<M and visit[x+dx[i]][y+dy[i]][wall] == 0: #끝에 부딪히지 않고 안가봤던 길인경우
                if Map[x+dx[i]][y+dy[i]] == '0': #길이 이동가능한곳인경우
                    visit[x+dx[i]][y+dy[i]][wall] = visit[x][y][wall]+1 #이전좌표의 값 +1 만큼 방문 표시함
                    q.append([x+dx[i],y+dy[i],wall]) #큐에 추가
                if wall ==0 and Map[x+dx[i]][y+dy[i]] == '1': #벽을 아직 안넘어봤고, 이동가능하지 않은 곳인경우
                    visit[x+dx[i]][y+dy[i]][1] = visit[x][y][0] +1 #이전좌표 +1 만큼 방문 표시함
                    q.append([x+dx[i],y+dy[i],1]) #큐에 추가하는데, wall은 1로 업데이트

    return -1
                    
N,M = map(int,input().split())
Map = [list(input())for _ in range(N)]
q = deque()
q.append([0,0,0])

print(bfs())