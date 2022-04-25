case = int(input())
case_list = list(str(case))
case_len = len(case_list)
answer = 99
if case_len < 3 :
    print(case)
else :
    for i in range(100,case+1):
        num_list = list(map(int,list(str(i))))
        if num_list[0]-num_list[1] == num_list[1]-num_list[2] :
            answer +=1
    print(answer)


