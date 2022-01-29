a= input().split()
a = list(map(int,a))

i = 1
if a[2] <= a[1] :
    print('-1')
else :
    print(int(a[0] / (a[2]-a[1])) +1)
    

