from collections import deque
size = 2
eat_fish = 0
timer = 0
N = int(input())
area = [list(map(int,input().split())) for _ in range(N)]
dir_ = [(-1,0),(0,-1),(0,1),(1,0)] #상 좌 우 하
for i in range(N):
    for j in range(N): 
        if area[i][j] == 9:
            shark_position = (i,j)
            area[i][j] = 0
        # if area[i][j] != 0 and area[i][j] != 9 and area[i][j] in fishes:
        #     fishes[area[i][j]].append((i,j))
        # elif area[i][j] != 0 and area[i][j] != 9 and area[i][j] not in fishes:
        #     fishes[area[i][j]] = [(i,j)]
#---------------세팅완료----------------


while True:
    for i in area:
        print(i)
    print()
    
    fishes = []
    is_break = False
    is_changed = False
    q = deque([shark_position]) 
    visited = [[0]*N for _ in range(N)]
    visited[shark_position[0]][shark_position[1]] = 1
    
    while q:
        if is_break : break
        row,col = q.popleft()
        for i in dir_:
            dr = row + i[0]
            dc = col + i[1]
            if 0<=dr<N and 0<=dc < N and visited[dr][dc] == 0:
                if area[dr][dc] ==0 or area[dr][dc] == size : 
                    q.append((dr,dc))
                    visited[dr][dc] = visited[row][col] + 1
                elif area[dr][dc] < size:
                    
                    shark_position = (dr,dc)
                    eat_fish += 1
                    if eat_fish == size:
                        size+=1
                        eat_fish = 0
                    area[dr][dc] = 0
                    timer += visited[row][col] 
                    print(timer)
                    is_break = True
                    is_changed = True
                    break
    if not is_changed:
        print(timer)
        break
            
    




            