def solution(N, stages):
    fail_rate = {}
    stages.sort()
    stage_sort=(list(set(stages)))
    for i in range(1,N+1):
        if i in stages :
            fail_rate[i]=(stages.count(i)/len(stages[stages.index(i):]))
        else:
            fail_rate[i]=0
    fail_rate = dict(sorted(fail_rate.items(),key = lambda x : x[1],reverse=True))

    
    answer = list(fail_rate.keys())
    return answer