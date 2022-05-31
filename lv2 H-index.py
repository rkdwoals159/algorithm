def solution(citations):
    citations.sort()
    answer = 0
    for idx,h in enumerate(citations):
        if h <= len(citations)-idx : answer = h
        else: 
            if answer < len(citations)-idx: return len(citations)-idx
            else: return answer
    return answer