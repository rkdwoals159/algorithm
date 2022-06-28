import copy
array_len = int(input())
case = [list(map(int,input().split())) for _ in range(array_len)]

def up(cnt) :
    global case
    global max_num
    if cnt ==5 : 
        max_num = max(max_num,max(list(map(max,case))))  
        return
    up_case = [[case[i][j] for i in range(array_len)] for j in range(array_len)] 

    for i in up_case: ## 전부 위로 모아줌
        cnt_zero = 0
        for idx in range(len(i)):
            idx = idx - cnt_zero
            if i[idx] == 0:
                i.append(i.pop(idx))
                cnt_zero+=1

    for i in up_case:
        for idx in range(len(i)):
            if idx ==0: continue
            if i[idx] == i[idx-1] :
                i[idx-1] += i[idx-1]
                i[idx] = 0

    for i in up_case: ## 전부 위로 모아줌
        cnt_zero = 0
        for idx in range(len(i)):
            idx = idx - cnt_zero
            if i[idx] == 0:
                i.append(i.pop(idx))
                cnt_zero+=1

    case = [[up_case[i][j] for i in range(array_len)] for j in range(array_len)] 
    
    
    tmp = copy.deepcopy(case)
    up(cnt+1)
    case = copy.deepcopy(tmp)
    right(cnt+1)
    case = copy.deepcopy(tmp)
    down(cnt+1)
    case = copy.deepcopy(tmp)
    left(cnt+1)
    case = copy.deepcopy(tmp)
    
def right(cnt) :
    global case
    global max_num
    if cnt ==5 : 
        max_num = max(max_num,max(list(map(max,case))))  
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


    tmp = copy.deepcopy(case)
    up(cnt+1)
    case = copy.deepcopy(tmp)
    right(cnt+1)
    case = copy.deepcopy(tmp)
    down(cnt+1)
    case = copy.deepcopy(tmp)
    left(cnt+1)
    case = copy.deepcopy(tmp)
    
    
    
def left(cnt) :
    global case
    global max_num
    if cnt ==5 : 
        max_num = max(max_num,max(list(map(max,case))))  

    for i in case: ## 전부 위로 모아줌
            cnt_zero = 0
            for idx in range(len(i)):
                idx = idx - cnt_zero
                if i[idx] == 0:
                    i.append(i.pop(idx))
                    cnt_zero+=1

    for i in case:
        for idx in range(len(i)):
            if idx == 0 :continue
            if i[idx] == i[idx-1]:
                i[idx-1] += i[idx-1]
                i[idx] = 0
    for i in case: ## 전부 위로 모아줌
            cnt_zero = 0
            for idx in range(len(i)):
                idx = idx - cnt_zero
                if i[idx] == 0:
                    i.append(i.pop(idx))
                    cnt_zero+=1


    tmp = copy.deepcopy(case)
    up(cnt+1)
    case = copy.deepcopy(tmp)
    right(cnt+1)
    case = copy.deepcopy(tmp)
    down(cnt+1)
    case = copy.deepcopy(tmp)
    left(cnt+1)
    case = copy.deepcopy(tmp)

def down(cnt) :
    global case
    global max_num
    if cnt ==5 : 
        max_num = max(max_num,max(list(map(max,case))))  
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
    
    
    
    tmp = copy.deepcopy(case)
    up(cnt+1)
    case = copy.deepcopy(tmp)
    right(cnt+1)
    case = copy.deepcopy(tmp)
    down(cnt+1)
    case = copy.deepcopy(tmp)
    left(cnt+1)
    case = copy.deepcopy(tmp)
    
    
max_num = 0
tmp = copy.deepcopy(case)
up(0)
case = copy.deepcopy(tmp)
right(0)
case = copy.deepcopy(tmp)
left(0)
case = copy.deepcopy(tmp)
down(0)


print(max_num)

