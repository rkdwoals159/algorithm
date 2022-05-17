N = int(input())
case = list(map(int,input().split()))
answer =[]
S = int(input())
while S > 0:
    max_Idx = case.index(max(case[:S+1]))
    answer.append(case.pop(max_Idx))
    S -= max_Idx
    if not case : break
answer.extend(case)
print(*answer)


