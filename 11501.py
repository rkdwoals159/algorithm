import sys

T = int(sys.stdin.readline())
T_C = []

for _ in range(T):
    T_C.append(int(sys.stdin.readline()))
    T_C.append(sys.stdin.readline().rstrip())

while T_C:
    answer = 0
    max_num = 0
    N = T_C.pop(0)
    case = list(map(int,T_C.pop(0).split()))
    for i in reversed(case):
        if i > max_num:
            max_num = i
        else:
            answer += max_num - i
    print(answer)