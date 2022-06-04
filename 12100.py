from collections import deque
array_len = int(input())
case = [list(map(int,input().split())) for _ in range(array_len)]

def up(cnt) :
    global case
    global max_num
    if cnt ==5 : 
        if max_num < max(list(map(max,case))): max_num = max(list(map(max,case)))
        return
    up_case = [[case[i][j] for i in range(array_len)] for j in range(array_len)] 
    for i in up_case:
        print(i)
    print()
    for i in up_case: ## 전부 위로 모아줌
        for idx in range(len(i)):
            if i[idx] == 0:
                i.append(i.pop(idx))
    for i in up_case:
        print(i)
    print()
    for i in up_case:
        for idx in range(len(i)):
            if idx ==0: continue
            if i[idx] == i[idx-1] :
                i[idx-1] += i[idx-1]
                i[idx] = 0

    for i in up_case: ## 전부 위로 모아줌
        for idx in range(len(i)):
            if i[idx] == 0:
                i.append(i.pop(idx))

    case = [[up_case[i][j] for i in range(array_len)] for j in range(array_len)] 
    # up(cnt+1)
    # right(cnt+1)
    # down(cnt+1)
    # left(cnt+1)

def right(cnt) :
    global case
    global max_num
    if cnt ==5 : 
        if max_num < max(list(map(max,case))): max_num = max(list(map(max,case)))
        return
    for i in case:
        for idx in range(len(i)):
            if i[idx] == 0:
                i.insert(0,i.pop(idx))
    
    for i in case:
        for idx in range(len(i)-1,-1,-1):
            if idx == len(i)-1: continue
            if i[idx] == i[idx+1]:
                i[idx+1] += i[idx+1]
                i[idx] = 0
    
    for i in case:
        for idx in range(len(i)):
            if i[idx] == 0:
                i.insert(0,i.pop(idx))

    # up(cnt+1)
    # right(cnt+1)
    # down(cnt+1)
    # left(cnt+1)

def left(cnt) :
    global case
    global max_num
    if cnt ==5 : 
        if max_num < max(list(map(max,case))): max_num = max(list(map(max,case)))
        return
    for i in case:
        for idx in range(len(i)):
            if i[idx] == 0:
                i.append(i.pop(idx))

    for i in case:
        for idx in range(len(i)):
            if idx == 0 :continue
            if i[idx] == i[idx-1]:
                i[idx-1] += i[idx-1]
                i[idx] = 0
    for i in case:
        for idx in range(len(i)):
            if i[idx] == 0:
                i.append(i.pop(idx))


    # up(cnt+1)
    # right(cnt+1)
    # down(cnt+1)
    # left(cnt+1)

def down(cnt) :
    global case
    global max_num
    if cnt ==5 : 
        if max_num < max(list(map(max,case))): max_num = max(list(map(max,case)))
        return
    down_case = [[case[i][j] for i in range(array_len)] for j in range(array_len)] 

    for i in down_case:
        for idx in range(len(i)):
            if i[idx] == 0:
                i.insert(0,i.pop(idx))
    
    for i in down_case:
        for idx in range(len(i)):
            if idx == len(i)-1: continue
            if i[idx] == i[idx+1]:
                i[idx+1] += i[idx+1]
                i[idx] = 0
    
    for i in down_case:
        for idx in range(len(i)):
            if i[idx] == 0:
                i.insert(0,i.pop(idx))
    
    case = [[down_case[i][j] for i in range(array_len)] for j in range(array_len)] 

    # up(cnt+1)
    # right(cnt+1)
    # down(cnt+1)
    # left(cnt+1)
max_num = 0
up(0)
# right(0)
# left(0)
# down(0)

for i in case:
    print(i)
print(max_num)

