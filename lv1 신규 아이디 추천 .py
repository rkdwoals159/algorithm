def solution(new_id):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    answer = ''
    #1
    new_id = new_id.lower()
    #2
    for i in new_id:
        if i in alp or i in num or i == '-' or i=='_' or i=='.' :
            answer += i
    new_id = answer

    #3
    period = False
    answer = ''
    for i in new_id:
        if i == '.' :
            period = True
        else: 
            if period == True:
                answer += '.' + i 
                period = False
            else : answer += i
    #4
    if answer :
        if answer[0] == '.' : 
            tmp = list(answer)
            tmp[0] = ''
            answer = ''.join(tmp)
        if answer[-1] == '.' : 
            tmp = list(answer)
            tmp[-1] = ''
            answer = ''.join(tmp)
    
    #5
    if answer : pass 
    else : answer = 'a'
    
    #6
    if len(answer) >= 16 :
        answer = answer[:15]
        if answer[-1] == '.' : 
            tmp = list(answer)
            tmp[-1] = ''
            answer = ''.join(tmp)
    #7
    if len(answer) <=2 :
        while len(answer) < 3 :
            answer += answer[-1]
            
            
    return answer