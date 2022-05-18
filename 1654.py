N,M = map(int,input().split())
case = []
for _ in range(N):
    case.append(int(input()))
num = max(case) // 2
max_range = max(case)
can_add_1 = False
while True:
    if num == 0: num = 1
    tmp = num
    sum = 0
    for i in case:
        sum += i // num
    if sum >= M:
        num = (num+max_range)//2
    else: 
        max_range = num
        num = num//2
    if tmp==num and can_add_1 ==True:
        break
    elif can_add_1 ==True: 
        tmp -=1
        break
    if tmp == num and can_add_1 == False: 
        can_add_1 = True
        num +=1

print(tmp)
