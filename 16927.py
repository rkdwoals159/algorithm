#N 혹은 M길이가 1또는 2가 나오면 완전 반복 완료된것임.
from collections import deque
N,M,R = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(N)]
n = N
m = M

def rotate(idx,N):
    
    if idx == 0:
        tmp_top = deque(area[idx])
    else : tmp_top = deque(area[idx][idx:-idx])
    tmp_top.append(tmp_top.popleft()) # 2개 9 8 -> 1개 9
    
    tmp_left = deque([area[idx+i][idx] for i in range(1,N)]) #2개
    tmp_left.appendleft(tmp_top.pop()) #3개 8 14 20 -> 2개 8 14
    
    if idx == 0:
        tmp_bottom = deque(area[-1][idx+1:]) #1개 21
    else : tmp_bottom = deque(area[-idx-1][idx+1:-idx]) #1개 21
    tmp_bottom.appendleft(tmp_left.pop()) # 2개 20 21
    
    tmp_right = deque([area[idx+i][-idx-1] for i in range(N-1)]) #2개 9 15
    tmp_right.append(tmp_bottom.pop())
    tmp_right.popleft() #2개 15 21
    
    tmp_top = list(tmp_top)
    tmp_bottom = list(tmp_bottom)
    tmp_left = list(tmp_left)
    tmp_right = list(tmp_right)
    

    
    #덮어씌우기
    if idx == 0:
        area[0][:-1] = tmp_top[:]
        area[-1][1:] = tmp_bottom[:]
    else:
        area[idx][idx:-idx-1] = tmp_top[:]
        area[-idx-1][idx+1:-idx] = tmp_bottom[:]
    for i in range(1,N):
        area[idx+i][idx] = tmp_left[i-1]
    for i in range(N-1):
        area[idx+i][-idx-1] = tmp_right[i]
    

  
for _ in range(R):
    idx = 0
    N = n
    M = m
    while N >= 1 and M >= 1 :
        rotate(idx,N)
        N-=2
        M-=2
        idx +=1

for i in area:
    print(*i)
        
        




    
            
    


    
