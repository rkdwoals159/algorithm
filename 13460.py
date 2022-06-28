# N,M = map(int,input().split())
# maze = [list(input()) for _ in range(N)]
# answer = 99


# def left_change(List,target_idx,marble): #왼쪽으로 기울었을때 구슬의 움직임
#     target_start = target_idx
#     while List[target_idx-1] == '.':
#         target_idx -=1
#     if target_start != target_idx: #구슬이 한칸이라도 움직였을 경우
#         List[target_idx] = marble
#         List[target_start] = '.'
#     return List

# def right_change(List,target_idx,marble): #왼쪽으로 기울었을때 구슬의 움직임
#     target_start = target_idx
#     while List[target_idx+1] == '.':
#         target_idx +=1
#     if target_start != target_idx: #구슬이 한칸이라도 움직였을 경우
#         List[target_idx] = marble
#         List[target_start] = '.'
#     return List
    


# def up(Area,cnt) :
#     global answer
#     if cnt == 11 :
#         if answer == 99 :
#             answer = -1
#         return

    
#     up_area = [list(map(lambda x: x[i], Area)) for i in range(M)]
#     #빨간구슬 이동 :
#     for i in up_area:
#         if 'O' in i and 'R' in i and 'B' in i:
#             if i.index('O') < i.index('R') and i.index('O') < i.index('B'):
#                 return
                     
#         if  'R' in i:
#             if 'O' in i and i.index('O') < i.index('R'):
#                 answer = min(answer,cnt)
#                 return 
#             else: i = left_change(i,i.index('R'),'R')
            
#         if 'B' in i :
#             if 'O' in i and i.index('O') < i.index('B'):
#                 return 
#             else: i = left_change(i,i.index('B'),'B')
            
#         if  'R' in i: #R보다 B가 더 앞에있어서 못움직였을 경우를 대비해 한번더 처리해줌
#             i = left_change(i,i.index('R'),'R')
            
#     Area = [list(map(lambda x: x[i], up_area)) for i in range(N)]
    
#     up(Area,cnt+1)
#     down(Area,cnt+1)
#     right(Area,cnt+1)
#     left(Area,cnt+1)

# def down(Area,cnt) :
#     global answer
#     if cnt == 11 :
#         if answer == 99 :
#             answer = -1
#         return

#     down_area = [list(map(lambda x: x[i], Area)) for i in range(M)]
#     #빨간구슬 이동 :
#     for i in down_area:
#         if 'O' in i and 'R' in i and 'B' in i:
#             if i.index('O') > i.index('R') and i.index('O') > i.index('B'):
#                 return
                     
#         if  'R' in i:
#             if 'O' in i and i.index('O') > i.index('R'):
#                 answer = min(answer,cnt)
#                 return 
#             else: i = right_change(i,i.index('R'),'R')
            
#         if 'B' in i :
#             if 'O' in i and i.index('O') > i.index('B'):
#                 return 
#             else: i = right_change(i,i.index('B'),'B')
            
#         if  'R' in i: #R보다 B가 더 앞에있어서 못움직였을 경우를 대비해 한번더 처리해줌
#             i = right_change(i,i.index('R'),'R')
            
#     Area = [list(map(lambda x: x[i], down_area)) for i in range(N)]

#     up(Area,cnt+1)
#     down(Area,cnt+1)
#     right(Area,cnt+1)
#     left(Area,cnt+1)

# def right(Area,cnt) :
#     global answer
#     if cnt == 11 :
#         if answer == 99 :
#             answer = -1
#         return

#     for i in Area:
#         if 'O' in i and 'R' in i and 'B' in i:
#             if i.index('O') > i.index('R') and i.index('O') > i.index('B'):
#                 return
#         #빨간구슬 이동 :    
#         if  'R' in i:
#             if 'O' in i and i.index('O') > i.index('R'):
#                 answer = min(answer,cnt)
#                 return 
#             else: i = right_change(i,i.index('R'),'R')
            
#         if 'B' in i :
#             if 'O' in i and i.index('O') > i.index('B'):
#                 return 
#             else: i = right_change(i,i.index('B'),'B')
            
#         if  'R' in i: #R보다 B가 더 앞에있어서 못움직였을 경우를 대비해 한번더 처리해줌
#             i = right_change(i,i.index('R'),'R')

#     up(Area,cnt+1)
#     down(Area,cnt+1)
#     right(Area,cnt+1)
#     left(Area,cnt+1)
            
# def left(Area,cnt) :
#     global answer
#     if cnt == 11 :
#         if answer == 99 :
#             answer = -1
#         return


#     #빨간구슬 이동 :
#     for i in Area:
#         if 'O' in i and 'R' in i and 'B' in i:
#             if i.index('O') < i.index('R') and i.index('O') < i.index('B'):
#                 return
                     
#         if  'R' in i:
#             if 'O' in i and i.index('O') < i.index('R'):
#                 answer = min(answer,cnt)
#                 return 
#             else: i = left_change(i,i.index('R'),'R')
            
#         if 'B' in i :
#             if 'O' in i and i.index('O') < i.index('B'):
#                 return 
#             else: i = left_change(i,i.index('B'),'B')
            
#         if  'R' in i: #R보다 B가 더 앞에있어서 못움직였을 경우를 대비해 한번더 처리해줌
#             i = left_change(i,i.index('R'),'R')
#     up(Area,cnt+1)
#     down(Area,cnt+1)
#     right(Area,cnt+1)
#     left(Area,cnt+1)

# def start(cnt):
#     up(maze,cnt)
#     down(maze,cnt)
#     right(maze,cnt)
#     left(maze,cnt)
#     print(answer)
# start(1)

N,M = map(int,input().split())
maze = [list(input()) for _ in range(N)]
answer = 99

for i in maze:
    if 'R' in i:
        R_x = i.index('R')
        R_y = maze.index(i)
    if 'B' in i:
        B_x = i.index('B')
        B_y = maze.index(i)
maze[R_y][R_x] = '.'
maze[B_y][B_x] = '.'


def left_change(List,target_idx): #왼쪽으로 기울었을때 구슬의 움직임
    while List[target_idx-1] == '.':
        target_idx -=1
    return target_idx

def right_change(List,target_idx): #왼쪽으로 기울었을때 구슬의 움직임
    while List[target_idx+1] == '.':
        target_idx +=1
    return target_idx

def up(cnt,R_x,R_y,B_x,B_y):
    global answer
    if cnt == 11:
        # if answer == 99:
        #     answer = -1
        return
    B_up_list = [maze[idx][B_x] for idx in range(M)]
    R_up_list = [maze[idx][R_x] for idx in range(M)]
    
    if B_up_list == R_up_list:
        if 'O' in B_up_list:
            if B_up_list.index('O') < R_y and B_up_list.index('O') < B_y:
                return
        elif R_y < B_y: 
            R_y = left_change(R_up_list,R_y)
            B_y = left_change(B_up_list,B_y)
        else: 
            B_y = left_change(B_up_list,B_y)
            R_y = left_change(R_up_list,R_y)
    #빨간 구슬 이동   
    if 'O' in R_up_list and R_up_list.index('O') < R_y:
        answer = min(answer,cnt)
        return 
    else: R_y = left_change(R_up_list,R_y)
    #파란 구슬 이동    
    if 'O' in B_up_list and B_up_list.index('O') < B_y:
        return 
    else: B_y = left_change(B_up_list,B_y)
    print("up!",[R_y,R_x],[B_y,B_x])
    
    up(cnt+1,R_x,R_y,B_x,B_y)
    down(cnt+1,R_x,R_y,B_x,B_y)
    left(cnt+1,R_x,R_y,B_x,B_y)
    right(cnt+1,R_x,R_y,B_x,B_y)

def down(cnt,R_x,R_y,B_x,B_y):
    global answer
    if cnt == 11:
        # if answer == 99:
        #     answer = -1
        return
    B_up_list = [maze[idx][B_x] for idx in range(M)]
    R_up_list = [maze[idx][R_x] for idx in range(M)]
    
    if B_up_list == R_up_list:
        if 'O' in B_up_list:
            if B_up_list.index('O') > R_y and B_up_list.index('O') > B_y:
                return
        elif R_y > B_y: 
            R_y = right_change(R_up_list,R_y)
            B_y = right_change(B_up_list,B_y)
        else: 
            B_y = right_change(B_up_list,B_y)
            R_y = right_change(R_up_list,R_y)
    #빨간 구슬 이동   
    if 'O' in R_up_list and R_up_list.index('O') > R_y:
        answer = min(answer,cnt)
        return 
    else: R_y = right_change(R_up_list,R_y)
    #파란 구슬 이동    
    if 'O' in B_up_list and B_up_list.index('O') > B_y:
        return 
    else: B_y = right_change(B_up_list,B_y)
    print("down!",[R_y,R_x],[B_y,B_x])
    up(cnt+1,R_x,R_y,B_x,B_y)
    down(cnt+1,R_x,R_y,B_x,B_y)
    left(cnt+1,R_x,R_y,B_x,B_y)
    right(cnt+1,R_x,R_y,B_x,B_y)
def left(cnt,R_x,R_y,B_x,B_y):
    global answer
    if cnt == 11:
        # if answer == 99:
        #     answer = -1
        return
    if maze[B_y] == maze[R_y]:
        if 'O' in maze[B_y]:
            if maze[B_y].index('O') < R_x and maze[B_y].index('O') < B_x:
                return
        elif R_x < B_x: 
            R_x = left_change(maze[B_y],R_x)
            B_x = left_change(maze[B_y],B_x)
        else: 
            B_x = left_change(maze[B_y],B_x)
            R_x = left_change(maze[B_y],R_x)
    #빨간 구슬 이동   
    if 'O' in maze[R_y] and maze[R_y].index('O') < R_x:
        answer = min(answer,cnt)
        return 
    else: R_x = left_change(maze[R_y],R_x)
    #파란 구슬 이동    
    if 'O' in maze[B_y] and maze[B_y].index('O') < B_x:
        return 
    else: B_x = left_change(maze[B_y],B_x)
    print("left!",[R_y,R_x],[B_y,B_x])
    up(cnt+1,R_x,R_y,B_x,B_y)
    down(cnt+1,R_x,R_y,B_x,B_y)
    left(cnt+1,R_x,R_y,B_x,B_y)
    right(cnt+1,R_x,R_y,B_x,B_y)
def right(cnt,R_x,R_y,B_x,B_y):
    global answer
    if cnt == 11:
    #     if answer == 99:
    #         answer = -1
        return
    if maze[B_y] == maze[R_y]:
        if 'O' in maze[B_y]:
            if maze[B_y].index('O') > R_x and maze[B_y].index('O') > B_x:
                return
        elif R_x > B_x: 
            R_x = right_change(maze[B_y],R_x)
            B_x = right_change(maze[B_y],B_x)
        else: 
            B_x = right_change(maze[B_y],B_x)
            R_x = right_change(maze[B_y],R_x)
    #빨간 구슬 이동   
    if 'O' in maze[R_y] and maze[R_y].index('O') > R_x:
        answer = min(answer,cnt)
        return 
    else: R_x = right_change(maze[R_y],R_x)
    #파란 구슬 이동    
    if 'O' in maze[B_y] and maze[B_y].index('O') > B_x:
        return 
    else: B_x = right_change(maze[B_y],B_x)
    print("right!",[R_y,R_x],[B_y,B_x])
    up(cnt+1,R_x,R_y,B_x,B_y)
    down(cnt+1,R_x,R_y,B_x,B_y)
    left(cnt+1,R_x,R_y,B_x,B_y)
    right(cnt+1,R_x,R_y,B_x,B_y)
def start():
    up(1,R_x,R_y,B_x,B_y)
    down(1,R_x,R_y,B_x,B_y)
    left(1,R_x,R_y,B_x,B_y)
    right(1,R_x,R_y,B_x,B_y)
    print(answer)
start()