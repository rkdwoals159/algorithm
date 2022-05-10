# IOIOI 서브태스크다국어
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	16631	4957	3988	31.459%
# 문제
# N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.

# P1 IOI
# P2 IOIOI
# P3 IOIOIOI
# PN IOIOI...OI (O가 N개)
# I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.

# 출력
# S에 PN이 몇 군데 포함되어 있는지 출력한다.

# 제한
# 1 ≤ N ≤ 1,000,000
# 2N+1 ≤ M ≤ 1,000,000
# S는 I와 O로만 이루어져 있다.
# 서브태스크
# 번호	배점	제한
# 1	50	
# N ≤ 100, M ≤ 10 000.

# 2	50	
# 추가적인 제약 조건이 없다.

# 예제 입력 1 
# 1
# 13
# OOIOIOIOIIOII
# 예제 출력 1 
# 4
#50점짜리 단순 반복
# import sys

# N = int(sys.stdin.readline().rstrip()) #정수 N
# M = int(sys.stdin.readline().rstrip()) #문자열의 길이
# P_n = 'IO' * N + 'I' #IO이 교대로 나오는 문자열 P_n   IOI는 P_1 IOIOI는 P_2
# S = sys.stdin.readline().rstrip() #제시된 문자열
# cnt = 0
# P_n_length = len(P_n)

# for i in range(M-P_n_length) :
#     if S[i:i+P_n_length] == P_n :
#         cnt +=1

# print(cnt)



# -------------------------------------------------------------------------
import sys

# N = int(input())
# M = int(input())
# S = sys.stdin.readline().rstrip()

# answer, idx, count = 0, 0, 0

# while idx < (M - 1):
#     if S[idx : idx + 3] == 'IOI':
#         idx = idx + 2
#         count = count + 1
#         if count == N:
#             answer = answer + 1
#             count = count - 1
#     else:
#         idx = idx + 1
#         count = 0

# print(answer)


a,b = [sys.stdin.readline() for i in range(2)]
print(a)
print(b)