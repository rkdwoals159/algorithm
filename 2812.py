import sys
N,K = map(int,input().split())
case = sys.stdin.readline().rstrip()

MAX = int(max(case[:K]))
cnt = 0
for i in range(K) :
    if int(case[i]) < MAX :
        cnt +=1


    
