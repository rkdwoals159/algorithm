def solution(month, day, weeks):
    
    month_end = [0,31,28,31,30,31,30,31,31,30,31,30,31] #0월부터 12월까지 말일 리스트
    calender = [[0]*7 for _ in range(weeks)]

    total_days = 0
    for i in range(month):
        total_days += month_end[i]
    total_days += day


    start_day = (total_days-1) % 7 #스타트 지점의 인덱스는 전체 일수를 7로 나눈 나머지와 같다.
    calender[0][start_day]  = day

    #시작지점 왼쪽 먼저 채워준다.
    for i in range(start_day-1,-1,-1):
        calender[0][i] = calender[0][i+1] - 1
        if calender[0][i] == 0:
            calender[0][i] = month_end[month-1]


    #맨 앞부터 구현 시작.
    row = 0
    col = start_day
    month_cnt = 0 # 달력에서 달을 몇번 넘어갔는지 체크하기위한 변수
    if calender[0][0] > calender[0][start_day]:
        will_change = [(0,0,month-1)]
    else: will_change = [(0,0,month)]
    for idx in range(1,start_day):
        if calender[0][idx] == 1:
            will_change.append((0,idx,month))



    while col <= 6 and row < weeks:
        #12월 31일 도달시 break
        if month + month_cnt == 12 and calender[row][col] == 31:
            break
        #월말 넘어가면 1일로 돌림
        if calender[row][col] > month_end[month+month_cnt] :
            calender[row][col] = 1
            if month != 12 : month_cnt +=1
            will_change.append((row,col,month+month_cnt))

        #맨끝 도달시 break
        if col ==6 and row == weeks-1:
            break

        #달력채우기
        if col == 6:
            calender[row+1][0] = calender[row][col] + 1
            row +=1
            col = 0
        else:
            calender[row][col+1] = calender[row][col] + 1
            col +=1


    for r,c,m in will_change: #월/일 표시로 바꿔주기
        calender[r][c] = str(m) + '/' + str(calender[r][c])

    for r in range(weeks): #12월 31일 이후 0표시된 날들 다 필터로 걸러주기
        calender[r] = list(filter(lambda x: x !=0 , calender[r]))
        calender[r] = list(map(str,calender[r])) # 나머지 날들 int에서 str로 전환
    return calender

a= solution(5,1,1)
for i in a:
    print(i)