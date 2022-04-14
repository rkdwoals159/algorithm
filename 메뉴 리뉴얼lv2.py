from itertools import combinations
def solution(orders, course):
    answer = []
    for i in course:
        case = []
        
        for j in orders :
            case.extend(list(combinations(sorted(j),i)))
        if case:
            MAX = max(list(map(lambda x : case.count(x),case)))

            for k in case :
                l = ''.join(k)
                if MAX > 1 and case.count(k) == MAX and l not in answer :
                    answer.append(l)
    
                
    return sorted(answer)