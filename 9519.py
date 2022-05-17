import sys
N = int(input())
case = sys.stdin.readline().rstrip()
first_case = case #케이스 섞기전 순수한 맨처음 케이스 보존
suffle_list = [] #1~n번 섞은후 나온 값들을 담아놓는 리스트
cnt = 1
while True : #셔플 리스트에서 반복성이 나올시 종료
    is_odd = '' #홀수 모아둠
    is_even = ''#짝수 모아둠
    for idx,i in enumerate(case): #섞는 알고리즘
        if idx %2 == 1:
            is_odd +=i
        else: is_even +=i
    case = is_even + is_odd[::-1]
    suffle_list.append(case) #다섞은후 셔플리스트에 저장
    cnt +=1
    if first_case in suffle_list : break #섞은후 나온 케이스가 맨 처음케이스와 동일한경우, 한바퀴 반복이 돌았음으로 종료
print(suffle_list[(N%len(suffle_list))-1])

