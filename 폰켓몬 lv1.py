def solution(nums):
    answer = 0
    if len(list(set(nums))) >= len(nums)/2 :
        answer = len(nums)/2
    else :
        answer = len(list(set(nums)))
    

    return answer