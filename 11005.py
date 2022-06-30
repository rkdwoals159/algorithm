N,B = map(int,input().split())

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''
while True:
    N,K = divmod(N,B)
    if K>9: K = alp[K-10]
    answer += str(K)
    if N == 0 : break

print(answer[::-1])