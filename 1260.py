# DFS와 BFS
 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 2 초	128 MB	177169	63599	37570	35.105%
# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 예제 입력 1 
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 예제 출력 1 
# 1 2 4 3
# 1 2 3 4

from collections import deque

N,M,V = map(int,input().split())
vertex = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    vertex[a][b] = vertex[b][a] = 1
visit = [0]*(N+1)
def dfs(V):
    visit[V] = 1
    print(V,end=' ')
    for i in range(1,N+1):
        if visit[i]==0 and vertex[V][i] == 1:
            dfs(i)
       
def bfs(V):
    q = deque()
    q.append(V)   
    visit[V] = 0 
    while q:
        a = q.popleft()
        print(a,end=' ')
        for i in range(1,N+1):
            if visit[i]==1 and vertex[a][i] == 1:
                visit[i] = 0
                q.append(i)
dfs(V)
print()
bfs(V)