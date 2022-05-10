def solution(answers):
    answer = []
    case_1 = [1,2,3,4,5]
    case_2 = [2,1,2,3,2,4,2,5]
    case_3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    for i in range(len(answers)) :
        if case_1[i%5] == answers[i] :
            score[0]+=1
        if case_2[i%8] == answers[i] :
            score[1]+=1
        if case_3[i%10] == answers[i] :
            score[2]+=1
    for j in range(len(score)) :
        if score[j] == max(score):
            answer.append(j+1)

    return answer