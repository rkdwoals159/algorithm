def solution(arr):
    answer = []
    chk = -1
    for i in arr:
        if i == chk:
            pass
        else: 
            chk = i
            answer.append(i)
    return answer