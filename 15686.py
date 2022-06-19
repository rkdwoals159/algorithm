#치킨 리스트는 M개~13개 사이의 길이를 가지고있다.
#치킨 리스트에서 최대 M개의 가게를 살려야한다.
#M개까지의 백트래킹으로 인덱스를 구한후, 치킨집[인덱스]를 에있는 값을 
#distance_check에 넣으면 끝!


from collections import deque

N,M = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(N)]
dir_ = [(-1,0),(1,0),(0,1),(0,-1)]
house = []
chicken = []
answer = 99999
for i in range(N):
    for j in range(N):
        if area[i][j] == 1: house.append((i,j))
        elif area[i][j] == 2: 
            chicken.append((i,j))
            
def distance_check(save_chicken):
    global answer
    sum = 0
    for row,col in house:
        min_len = 99
        for i in save_chicken:
            r,c = chicken[i]
            min_len = min(min_len,abs(row - r) + abs(col - c))
        sum += min_len
    answer = min(answer,sum)
    
        
length = len(chicken)
def chicken_backtraking(idx,save_chicken,num,idx_end):
    if idx == idx_end:
        distance_check(save_chicken)
        return

    for i in range(num,length):
        save_chicken.append(i)
        chicken_backtraking(idx+1,save_chicken,i+1,idx_end)
        save_chicken.pop()
    

for m in range(1,M+1):
    chicken_backtraking(0,[],0,m)

print(answer)
    