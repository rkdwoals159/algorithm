def solution(numbers):
    case = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        case.remove(i)
    answer  = sum(case)
    return answer