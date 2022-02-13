case = []
for i in range(10000):
    a = i // 1000
    b = i // 100 - 10*a
    c = i // 10 - 10*b - 100*a
    d = i % 10
    case.append(a + b + c + d + i)

for i in range(10000) :
    if case.count(i) == 0 :
        print(i)
