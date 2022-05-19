def dfs(idx,computers,is_visited):
    is_visited[idx] = 1
    for cnt, i in enumerate(computers[idx]):
        if cnt == idx:
            continue
        if i == 1 and is_visited[cnt] == 0:
            dfs(cnt,computers,is_visited)
        
        
                    
def solution(n, computers):
    answer = 0
    is_visited = [0]*n
    
    for idx,i in enumerate(computers):
        if is_visited[idx] == 0:
            dfs(idx,computers,is_visited)
            answer +=1
    return answer