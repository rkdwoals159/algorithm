def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    lost_2 = []
    for i in lost :
        if i in reserve :
            reserve.remove(i)
        else: lost_2.append(i)
    for i in lost_2:
        if i-1 in reserve :
            reserve.remove(i-1)
        elif i+1 in reserve:
            reserve.remove(i+1)
        else :
            answer -=1
    return answer