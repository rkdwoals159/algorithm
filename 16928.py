#-------------------------dfs-------------------------
# N,M = map(int,input().split())
# edge = [list(map(int,input().split())) for _ in range(N+M)] #간선
# min_cnt = 99999999
# cnt = 0
# num = 1
# visited = [0] * 101
# def dfs(num,cnt):
#     global min_cnt
#     if visited[num] == 1: #이미 방문한 곳은 탐색 안함
#         return
#     else: visited[num] = 1

    # if num >=94: #주사위로 한방에 갈 수 있는곳은
    #     if num != 100: cnt+=1 #이미 100이라면 그냥 cnt안늘려야하니까
    #     if cnt < min_cnt: #최종 카운트가 미니엄보다 낮다면
    #         min_cnt = cnt #새로 갱신
    #     return
    # else: #주사위 6으로 한방에 못가는곳은
    #     for i in edge: #간선을 탐색해서
    #         if 0 <= (i[0] - num) and (i[0] - num) <= 6: # 6칸 이내에 사다리나 뱀이 있다면
    #             dfs(i[1],cnt+1) #휘리리릭
    #     dfs(num+6,cnt+1)#6칸 앞으로 이동

# dfs(1,0)
# print(min_cnt)


#-------------------------dfs-------------------------
# from collections import deque
# N,M = map(int,input().split())
# edge = [0] * 101
# visited = [0] * 101
# visited[1] = 1
# for _ in range(N+M):
#     a,b = map(int,input().split())
#     edge[a] = b
# num_queue = deque([1])
# while num_queue:
#     num = num_queue.popleft()
#     if num >=94: #주사위로 한방에 갈 수 있는곳은
#         if num != 100: visited[num]+=1 #이미 100이라면 카운트 안늘려야하니까
#         print(visited[num]-1)
#         break
#     else: #주사위 6으로 한방에 못가는곳은
#        for dice_number in range(1,7):
#             nv = num + dice_number
#             if edge[nv] :
#                 nv = edge[nv]
#             if not visited[nv] :
#                 visited[nv] = visited[num] + 1
#                 num_queue.append(nv)



from collections import deque
N,M = map(int,input().split())
edge = [0] * 101
visited = [0] * 101
visited[1] = 1
for _ in range(N+M):
    a,b = map(int,input().split())
    edge[a] = b
num_queue = deque([1])
while num_queue:
    num = num_queue.popleft()
    if num >=94: #주사위로 한방에 갈 수 있는곳은
        if num != 100: visited[num]+=1 #이미 100이라면 카운트 안늘려야하니까
        print(visited[num]-1)
        break
    else: #주사위 6으로 한방에 못가는곳은
       for dice_number in range(1,7):
            if  edge[num+dice_number] and not visited[edge[num+dice_number]] :
                visited[edge[num+dice_number]] = visited[num] + 1
                num_queue.append(edge[num+dice_number])

            elif not visited[num+dice_number] :
                visited[num+dice_number] = visited[num] + 1
                num_queue.append(num+dice_number)
                











# for i in range(10):
#     for j in range(10):
#         print(visited[10*i+j],end= ' ')



