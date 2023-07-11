case = []
for _ in range(3):
    case.append(input())

a,b,c = map(int, case)    
if(a+b+c != 180) : print('Error')
elif(a == 60 and b ==60 and c == 60) : print("Equilateral")
elif(a != b and b!= c and a!=c) : print("Scalene")
else :print("Isosceles")