def solution(nums):
    answer = 0
    case = []
    def backtraking(tmp):
        if len(tmp) == 3:
            tmp_ = [i for i in tmp]
            case.append(tmp_)
            return
        for i in nums:
            if i not in tmp:
                tmp.append(i)
                backtraking(tmp)
                tmp.pop()

    backtraking([])
    case = list(map(lambda x: sorted(x), case))
    case = list(set(map(tuple,case)))
    
    for i in case:
        is_Prime = True
        num = sum(i)
        for j in range(2,int(num**(0.5)+1)):
            if num % j == 0 :
                is_Prime = False
                break
        if is_Prime : answer += 1
            
        
            

    return answer