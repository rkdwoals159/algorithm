# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# 예제 입력 1 
# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91
# 예제 출력 1 
# 40.000%
# 57.143%
# 33.333%
# 66.667%
# 55.556%


N = int(input())
lst1 = []
for i in range(N) :
    lst1.append(input())
for a in lst1 :
    lst = a.split()
    sum = 0
    count = 0
    for i in lst[1:] :
        sum+=int(i)
    for i in lst[1:] :
        if int(i) > sum/int(lst[0]) :
            count += 1
    perCent = count/int(lst[0]) * 100
    print('{:.3f}'.format(perCent),end='')
    print('%')

    