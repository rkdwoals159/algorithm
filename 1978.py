# 4
# 1 3 5 7

# 3

# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

import sys
N = int(input())
cnt = 0
case = list(map(int,input().split()))

for i in range(N) :
    if(case[i]==1) :continue
    isValid = True
    for j in range(2,int(case[i]**1/2)+1):
        if case[i] % j == 0 : isValid = False
    if(isValid): cnt +=1
print(cnt)
    
    
