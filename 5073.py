import sys
while (True):
    a,b,c = map(int,sys.stdin.readline().strip().split())
    if(a==0 and b ==0 and c ==0):break
    if(max(a,b,c)>=a+b+c-max(a,b,c)):
        print("Invalid")
        continue
    
    if(a==b and b==c and a==c) : print("Equilateral")
    elif(a!=b and b!=c and a!=c) : print("Scalene")
    else : print("Isosceles")
    