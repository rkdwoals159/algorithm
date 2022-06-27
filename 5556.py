N = int(input())
K = int(input())
tile = [list(map(int,input().split())) for _ in range(K)]

for c,r in tile:
    
    if c > int(N/2):
        c = N-c+1
    if r > int(N/2):
        r = N-r+1
    
    ans = (min(r,c)-1) % 3
    print(ans+1)
    
    