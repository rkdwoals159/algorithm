from collections import deque
N,L,R = map(int,input().split())

countries = [list(map(int,input().split())) for _ in range(N)]

dir_ = [(-1,0),(1,0),(0,1),(0,-1)]

def bfs(countries) :
    visited = [[0] * N for _ in range(N)]
    is_changed = False
    for row in range(N):
        for col in range(N):
            if visited[row][col] == 1: continue
            
            is_opened = []
            visited[row][col] = 1
            q = deque([(row,col)])
            while q:
                row,col = q.popleft()
                is_opened.append((row,col))
                for i in dir_:
                    dr = row + i[0]
                    dc = col + i[1]
                    
                    if 0<=dr<N and 0<=dc<N and visited[dr][dc] == 0:
                        if L<= abs(countries[dr][dc] - countries[row][col]) <= R :
                            visited[dr][dc] = 1
                            q.append((dr,dc))
            total_population = 0
            if len(is_opened)>1 : 
                for r,c in is_opened :
                    total_population +=  countries[r][c]
                for r,c in is_opened :
                    tmp = countries[r][c]
                    countries[r][c] = total_population // len(is_opened)
                    if countries[r][c] != tmp: 
                        is_changed = True
    return is_changed



cnt = 0
while True:
    is_changed = bfs(countries)
    if not is_changed : 
        # for i in countries:
        #     print(i)
        # print()
        print(cnt)
        break
    else: 
        cnt +=1
        