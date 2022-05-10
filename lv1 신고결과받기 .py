def solution(id_list, report, k):
    answer = [0] * len(id_list) # user들이 받은 결과 메일의 수
    report= list(set(report))#신고내역들의 중복 제거
    square = [[0]*len(id_list) for _ in range(len(id_list))] #세로: 신고당한자 가로: 신고자
    for tmp in report :
        reporter, reported = tmp.split()
        a = id_list.index(reported)
        b = id_list.index(reporter)
        square[a][b] = 1
    
    for report_Mail_Target in range(len(id_list)) :
        if sum(square[report_Mail_Target][:]) >= k: #만일 신고당한자 열의 합이 k이상이라면
            for user in range(len(id_list)) : #그 열에서 값이 1인 행만을 찾아서 
                if square[report_Mail_Target][user] == 1:
                    answer[user] +=1 #그 행에 해당하는 유저에게 메일을 보내야하므로 +1
        

            
    return answer