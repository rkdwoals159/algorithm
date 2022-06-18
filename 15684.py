# 완탐으로 하고, 1개 2개 3개 사다리 넣은다음에 결과 확인하기.

#기본세팅
N,M,H = map(int,input().split())
start = [i for i in range(1,N+1)]
hr = {}
lane_checker = []
answer = []
#hr 가로선 딕셔너리 만들어주기
for i in range(M): 
    a,b = map(int,input().split())
    if a in hr: #horizontal line
        hr[a].append(b)
    else: hr[a] = [b]
#만든 레인이 조건에 부합한지 체크해주는 함수
def lane_check(start,hr) : 
    for vr in start: #vertical line
        lane = vr #트랙의 레인
        for i in range(1,H+1):
            if i in hr:
                if lane in hr[i]:
                    lane +=1
                elif lane-1 in hr[i]:
                    lane -=1
        if lane == vr: continue
        else : return False
    return True

#이제 레인을 임의적으로 0개~3개 넣어주기 => 백트래킹 사용
#레인은 서로 같거나 이어지지 않아야함
def backtraking(idx,hr,row_,col_):
    # print(hr)
    if idx in answer: return
    if idx == 4: return
    if lane_check(start,hr) :
        # print(hr)
        answer.append(idx)
        return
    for col in range(col_,N):
        if row_ in hr: #딕셔너리 key에 row가 있을경우
            if col - 1 not in hr[row_] and col not in hr[row_]: #앞이랑 현재가 없어야하고, 
                if col == N-1: #마지막인 경우는 그냥 진행
                    hr[row_].append(col)
                    backtraking(idx+1,hr,row_,col)
                    hr[row_].pop()
                else: #마지막이 아닌경우는 뒤의 존재도 확인해야함
                    if col + 1 not in hr[row_]:
                        hr[row_].append(col)
                        backtraking(idx+1,hr,row_,col)
                        hr[row_].pop()
        else: 
            hr[row_] = [col]
            backtraking(idx+1,hr,row_,col)
            hr[row_].pop()                        
    for row in range(row_+1,H+1):
        for col in range(1,N):
            if row in hr: #딕셔너리 key에 row가 있을경우
                if col - 1 not in hr[row] and col not in hr[row]: #앞이랑 현재가 없어야하고, 
                    if col == N-1: #마지막인 경우는 그냥 진행
                        hr[row].append(col)
                        backtraking(idx+1,hr,row,col)
                        hr[row].pop()
                    else: #마지막이 아닌경우는 뒤의 존재도 확인해야함
                        if col + 1 not in hr[row]:
                            hr[row].append(col)
                            backtraking(idx+1,hr,row,col)
                            hr[row].pop()
                        
            else: 
                hr[row] = [col]
                backtraking(idx+1,hr,row,col)
                hr[row].pop()




backtraking(0,hr,1,1)
# print(answer)
if answer:
    print(min(answer))
else: print(-1)
