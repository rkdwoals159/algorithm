#1 2016년
def solution(a, b):
    Month = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    Week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    answer = ''
    sum = 0 
    for i in range(1,a) :
        sum += Month[i]
    sum += b
    answer = Week[(sum % 7)-1]
    return answer
#2 ﻿최소직사각형
def solution(sizes):
    sizes = list(map(sorted,sizes))
    x_list = list(map(lambda x: x[0],sizes))
    y_list = list(map(lambda x: x[1],sizes))
    return max(x_list) * max(y_list)
#3 문자열 내림차순으로 배치하기
def solution(s): return ''.join(sorted(s,reverse = True))
#4 문자열 다루기 기본
def solution(s): return True if (len(s) == 4 or len(s)==6) and s.isdecimal() else False
#5 서울에서 김서방 찾기
def solution(seoul): return '김서방은 ' + str(seoul.index('Kim')) + '에 있다'

#6 소수 찾기
def solution(n):
    answer = 0
    case = [True] * (n+1)
    case[0] = False
    case[1] = False
    
    for i in range(n):
        if case[i] == False: continue
        else:
            for i in range(i*2,n+1,i):
                case[i] = False
    
    for i in case:
        if i == True: answer +=1
    
    
    return answer


#7 수박수박수박수박수박수?
def solution(n): 
    answer = ''
    for i in range(1,n+1):
        if i %2 == 1: answer +='수'
        else : answer +='박'
    return answer
#8 문자열을 정수로 바꾸기
def solution(s): return int(s[1:]) if s[0] == '+' else int(s)


#9 시저 암호
def solution(s, n):
    upper_case = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lower_case = list('abcdefghijklmnopqrstuvwxyz')
    s= list(s)
    for i in range(len(s)):
        if s[i] in upper_case:
            s[i] = upper_case[(upper_case.index(s[i]) + n) % len(upper_case)]
        elif s[i] in lower_case:
            s[i] = lower_case[(lower_case.index(s[i]) + n) % len(lower_case)]
    return ''.join(s)
#10 약수의 합
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    return answer