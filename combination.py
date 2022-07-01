#케이스가 string인 경우
#permutation과 다른점은, for문에서의 idx를 계속 넘겨주면서, 중복되지 않게 체크를 해준다는 것.
answer = []
case = 'abcdefg'
def string_combination(case,result,idx):
    if len(result) == 4:
        answer.append(result)
        return
    for i in range(idx,len(case)):
        result += case[i]
        string_combination(case,result,i+1)
        result = result[:-1]

string_combination(case,'',0)
for i in answer:
    print(i)
    
    
#케이스가 list인 경우
#위와 동일하지만, 얕은복사 고려해서 answer2에 추가할때 [:]로 리스트 깊은 복사해준다.
answer2 = []
case2 = ['a','b','c','d','e','f','g']
def list_combination(case2,result2,idx):
    if len(result2) == 4:
        answer2.append(result2[:])
        return
    for i in range(idx,len(case2)):
        result2.append(case2[i])
        list_combination(case2,result2,i+1)
        result2.pop()


list_combination(case2,[],0)
for i in answer2:
    print(i)