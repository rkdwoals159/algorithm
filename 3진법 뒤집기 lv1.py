def solution(n):
    answer = 0
    cnt = 0
    while True :
        if n // (3**cnt) != 0:
            cnt +=1
        else: break
        
    ternary =[]
    for i in range(cnt-1,-1,-1) :
        ternary.append(n // (3**i)) 
        n -= (n//(3**i))*(3**i)

    for idx,num in enumerate(ternary) :
        answer += (3**idx) *num
    return answer


#모범 답안
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer