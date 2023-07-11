case = list(map(int,input().split()))

case.sort()

max = case[-1]
a,b = case[:2]


if(max >= a + b):
    max = a+b-1
    
print(a+b+max)