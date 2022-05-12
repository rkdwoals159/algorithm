def solution(strings, n):
    answer = []
    for i in range(97,123) :
        tmp =[]
        for j in strings:
            if j[n] == chr(i) :
                tmp.append(j)
        answer.extend(sorted(tmp))
    return answer