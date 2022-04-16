# 부분수열의 합
 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	256 MB	49542	22856	14637	44.253%
# 문제
# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

# 출력
# 첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

# 예제 입력 1 
# 5 0
# -7 -3 -2 5 8
# 예제 출력 1 
# 1




#1. 조합을 이용한완전탐색
from itertools import combinations
N,S = list(map(int,input().split()))
case = list(map(int,input().split()))
case_ = []
cnt = 0
for i in range(1,N+1) :
    for j in combinations(case,i):
        case_.append(j)

for k in case_ :
    if sum(k) == S : 
        cnt+=1
        
print(cnt)


#2 bfs를 이용한 완전탐색
def dfs(idx,sum):
    global answer
    if idx >= n :return
    sum += arr[idx]
    if sum == s:
        answer +=1
    dfs(idx+1,sum)
    dfs(idx+1,sum-arr[idx])
    
    
n,s = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0
dfs(0,0)
print(answer)