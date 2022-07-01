
#케이스가 string인 경우, shallow copy를 신경쓰지 않아도 된다.
case = 'abcdefg'
answer = []
def backtraking(case,result):
    if len(result) == 4:
        answer.append(result)
        return
    for i in case:
        if i not in result:
            result += i
            backtraking(case,result)
            result = result[:-1]
backtraking(case,'')
for i in answer:
    print(i)
    

#케이스가 list인 경우
case2 = ['a','b','c','d','e','f']
answer2 = []

def backtraking2(case2,result2):
    if len(result2) == 4:
        answer2.append(result2[:]) #위와 같으나 shallow copy 고려해서 deep copy로 해줘야함.
        return
    for i in case2:
        if i not in result2:
            result2.append(i)
            backtraking2(case2,result2)
            result2.pop()
            
backtraking2(case2,[])
for i in answer2:
    print(i)

