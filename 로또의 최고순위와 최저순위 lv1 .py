def solution(lottos, win_nums):
    answer = []
    base_answer = 0
    err_answer = 0
    for num in lottos:
        if num in win_nums: 
            base_answer += 1
        if num == 0 :
            err_answer += 1
    
    if (7 - base_answer - err_answer) == 7 :
        answer.append(6)
    else : answer.append(7 - base_answer - err_answer)
    
    if (7 - base_answer ) == 7 :
        answer.append(6)
    else : answer.append(7 - base_answer)
            
    return answer