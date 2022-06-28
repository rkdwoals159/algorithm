N,M = map(int,input().split())
case = [list(map(int,input())) for _ in range (N)]
if N<10 or M <10: 
    print(-1)
else:
    lst_10 = []
    answer = []
    for i in range(N):
        for j in range(M):
            if case[i][j] == 1:
                lst_10.append((i,j))
    tmp_lst_10 = lst_10[:]

    while lst_10:
        is_break = False
        distance = {}
        main_r, main_c = lst_10.pop()
        for r,c in tmp_lst_10:
            tmp = max(abs(r-main_r),abs(c-main_c))
            if tmp in distance:
                is_break = True
                break
            else: distance[tmp] = 1
        
        if not is_break:
            print(distance)
            is_all_in = True
            for i in range(1,10):
                if i  not in distance:
                    is_all_in = False
                    break
            if is_all_in == True:
                answer = [main_r,main_c]
                break
    if answer:
        print(*answer)
    else: print(-1)
    