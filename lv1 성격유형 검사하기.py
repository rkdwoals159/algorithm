def choiceToScore(alpToScore,score,survey,choice):
    if choice - 4 >=0:
        score[alpToScore[survey[1]]][survey[1]] += choice-4
    else :score[alpToScore[survey[0]]][survey[0]] += abs(choice-4)
    return score
def solution(survey, choices):
    answer = ''
    alpToScore={
        'A':3,
        'N':3,
        'C':1,
        'F':1,
        'M':2,
        'J':2,
        'R':0,
        'T':0
    }
    score = [{
        'R':0,
        'T':0
    },{
        'C':0,
        'F':0
    },{
        'J':0,
        'M':0
    },{
        'A':0,
        'N':0
    }]
    for idx in range(len(choices)):
        score = choiceToScore(alpToScore,score,survey[idx],choices[idx])
    print(score)
    for i in score:
        answer += max(i,key=i.get)
    return answer