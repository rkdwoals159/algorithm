a = input()
test_case = ''
cnt = []
test_cnt = 0
answer = 1001
end=True
for n in range(1,len(a)+1) : #input 글자수 만큼 반복
    over_10 = 0
    case = [a[i:i+n] for i in range(0,len(a),n) ] ## n자리의 글자수로 나눠서 리스트에 저장
    for i in range(len(case)) :
        if case[i] != test_case : #테스트 케이스와 일치하지 않으면
            test_case = case[i] # 테스트 케이스 변경
            if test_cnt != 0:
                cnt.append(test_cnt) # test_cnt 추가
                if test_cnt >= 9: 
                    over_10 +=1
            test_cnt = 0 #test_cnt 초기화
            end=True
        else : 
            test_cnt +=1 
            end=False
    if end == False :
        cnt.append(test_cnt)
        if test_cnt >= 9: 
            over_10 +=1
        test_cnt = 0

    
        
        
    if answer > len(a) - sum(cnt*n) + len(cnt) + over_10 :
        answer = len(a) - sum(cnt*n) + len(cnt) + over_10


    cnt.clear()
print(answer)

        