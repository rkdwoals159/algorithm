def solution(p):
    answer = ''
    
    def V2(p):
        if not p : return '' #p = ''인 경우 재귀 호출 종료
        op = 0 #열린 괄호의 개수
        cl = 0 #닫힌 괄호의 개수
        u = ''
        v = ''
        is_perfect = True #u가 옳은 괄호의 집합 인지 판별
        for i in range(len(p)):
            if p[i] =='(' : op +=1
            else: cl +=1
            if cl > op: is_perfect = False
            if op ==cl :
                if i+1 == len(p):
                    u = p
                    break
                else:
                    u = p[:i+1]
                    v = p[i+1:]
                    break
        v =V2(v) #재귀
        if is_perfect : return u+v #u 집합이 옳은 괄호여서 수정할 필요가 없다면, 바로 u+v 리턴
        else:
            tmp = '(' #문제의 순서에 따름
            tmp += v
            tmp += ')'
            for idx in range(1,len(u)-1) : #(와 )의 각자 방향 바꿔준다.
                if u[idx] == '(':
                    u =u[:idx] + ')' + u[idx+1:] 
                else: u =u[:idx] + '(' + u[idx+1:] 
            u = u[1:-1] #u집합의 양쪽 끝 제거
            tmp += u
            return tmp
    answer = V2(p)
    return answer