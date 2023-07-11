# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# 직사각형의 네 번째 점의 좌표를 출력한다.

# 5 5
# 5 7
# 7 5

# 7 7

x_container = []
y_container = []
answer = []
for _ in range(3) :
    X,Y = map(int,input().split())
    x_container.append(X)
    y_container.append(Y)

for i in range(3) : 
    if(x_container.count(x_container[i])==1):
         answer.append(x_container[i])
for i in range(3) : 
    if(y_container.count(y_container[i])==1):
         answer.append(y_container[i])

print(' '.join(str(ans) for ans in answer))