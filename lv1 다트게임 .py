def solution(dartResult):
    answer = 0
    case = []
    idx = 0
    tmp = 0
    is_ten = False
    for i in dartResult :
        if i == '0' and is_ten ==True: #확인해보니 10이네! 1을 10으로 바꿔준다
            tmp = 10
            is_ten = False
            continue
        if i in '0123456789':
            tmp = int(i)
            if tmp == 1 : is_ten = True #어 근데 이게 1이아니라 사실 10이라면? 다음걸 확인해보아야한다!
        elif i in 'SDT':
            is_ten = False
            if i =='S':
                case.append(tmp)
            elif i == 'D':
                case.append(tmp**2)
            else: case.append(tmp**3)
        else:
            is_ten = False
            if i =='#' :
                case[-1] = -case[-1]
            else :
                case[-1] *= 2
                if len(case) != 1: 
                    case[-2] *= 2
    answer = sum(case)
    return answer