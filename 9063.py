# 3
# 20 24
# 40 21
# 10 12

# 첫째 줄에는 점의 개수 N (1 ≤ N ≤ 100,000) 이 주어진다. 이어지는 N 줄에는 각 점의 좌표가 두 개의 정수로 한 줄에 하나씩 주어진다. 각각의 좌표는 -10,000 이상 10,000 이하의 정수이다. 


import sys
N = int(input())

min_x = 999999
min_y = 999999
max_x = -999999
max_y = -999999
for _ in range(N):
    x,y = map(int,sys.stdin.readline().strip().split())
    if min_x > x : min_x = x
    if min_y > y : min_y = y
    if max_x < x : max_x = x
    if max_y < y : max_y = y
    
print(abs((max_x-min_x)*(max_y-min_y)))