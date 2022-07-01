import sys

def left_rotate(number):
    if number>=1000:
        R,C = divmod(number,1000)
        number =  C*10 + R
    else: number = number *10
    return number

def right_rotate(number):
    R,C = divmod(number,10)
    number = R+C*1000
    return number

def Double(number):
    return (number * 2) % 10000

def Subtract(number):
    if number == 0:
        return 9999
    else:
        return number-1 


T = int(sys.stdin.readline())
test_case = [list(map(lambda x: x.zfill(4),sys.stdin.readline().split())) for _ in range(T)]
result = []
def bfs(case,q,answer,visited):
    visited[int(case)] = 1
    while q:
        tmp_case = int(case)
        com = q.pop(0)
        for i in com:
            if i == 'L' : 
                b = left_rotate(tmp_case)
                if b not in visited:
                    tmp_case = b
                    visited[b] = 1
            elif i == 'R' : 
                b = right_rotate(tmp_case)
                if b not in visited:
                    tmp_case = b
                    visited[b] = 1
            elif i == 'D' : 
                b = Double(tmp_case)
                if b not in visited:
                    tmp_case = b
                    visited[b] = 1
            elif i == 'S' : 
                b = Subtract(tmp_case)
                if b not in visited:
                    tmp_case = b
                    visited[b] = 1
        if tmp_case == int(answer): 
            return com
        q.append(com+'S')
        q.append(com+'L')
        q.append(com+'R')
        q.append(com+'D')
        
    return []
        

for case,answer in test_case:
    tmp_result=[]
    q = ['D','S','L','R']
    a = bfs(case,q,answer,{})
    if a: tmp_result.append(a)
    if tmp_result:
        result.append(sorted(tmp_result,key=len)[0])
for i in result:
    print(i)