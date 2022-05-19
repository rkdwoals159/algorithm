def solution(numbers, target):
    answer = 0
    def dfs(idx,tmp):
        nonlocal answer
        if idx == len(numbers):
            if tmp == target : answer +=1
            return
        tmp +=numbers[idx]
        dfs(idx+1,tmp)
        tmp -=numbers[idx]*2
        dfs(idx+1,tmp)
    dfs(0,0)
    
    return answer