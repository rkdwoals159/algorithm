# 첫째 줄에 다음 세 가지 중 하나를 출력한다.

# A가 B보다 큰 경우에는 '>'를 출력한다.
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.
# 제한
# -10,000 ≤ A, B ≤ 10,000
# 예제 입력 1 
# 1 2
# 예제 출력 1 
# <
# 예제 입력 2 
# 10 2
# 예제 출력 2 
# >
# 예제 입력 3 
# 5 5
# 예제 출력 3 
# ==

[a,b] = list(map(int,input().split()))

if a > b : print('>')
elif a<b : print('<')
else: print('=='
)