N = int(input())

case = []
for i in range(N):
    case.append(input())
case = list(set(case))
case.sort(key=lambda x: (len(x),x))
for i in case:
    print(i)