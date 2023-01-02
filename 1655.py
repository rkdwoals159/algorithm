import heapq
import sys
N = int(sys.stdin.readline())
answer = []
idx = 0
for _ in range(N):
    num = int(sys.stdin.readline())
    if idx>=2 and idx % 2 == 0:
        heapq.heappush(answer,num)
        heapq.heappop(answer)
        print(answer[0])
    else: 
        heapq.heappush(answer,num)
        print(answer[0])
    idx +=1