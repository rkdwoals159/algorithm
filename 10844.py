# N = int(input())
# idx = 0
# answer = 0

# def recur(idx,num):
#     global answer
#     if idx == N : 
#         answer +=1
#         return
#     if num != 0:
#         recur(idx+1,num-1)
#     if num != 9:
#         recur(idx+1,num+1)
# for i in range(1,10):
#     recur(1,i)
# print(answer) #시간초과
#----------------------------------------

N = int(input())

dp = [[0,0,0,0,0,0,0,0,0,0] for _ in range(N+1)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1,N):
    for j in range(10):
        if j>0 and j<9:
            dp[i+1][j] = dp[i][j-1] + dp[i][j+1]
        dp[i+1][0] = dp[i][1]
        dp[i+1][9] = dp[i][8]
print(sum(dp[N])%(10**9))
        

    
    