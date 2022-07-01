N = int(input())

cases = [list(input().split()) for _ in range(N)]

opcode = {'ADD':'0000','SUB':'0001','MOV':'0010','AND':'0011',
          'OR':'0100',"NOT":'0101','MULT':'0110','LSFTL':'0111',
          'LSFTR':'1000','ASFTR':'1001','RL':'1010','RR':'1011'}

def decoder(num):
    result =''
    while num > 0:
        num,R = divmod(num,2)
        result += str(R)
    return result[::-1].zfill(3)

for case in cases:
    answer =''
    if case[0][-1]== 'C':
        answer += opcode[case[0][:-1]]
        answer +='1'
    else: 
        answer += opcode[case[0]]
        answer +='0'
    answer += '0'
    for i in range(1,4):
        if i == 3 and case[0][-1] == 'C': 
            answer += decoder(int(case[3])).zfill(4)
            continue
        elif i == 3:
            answer += decoder(int(case[i]))
            answer +='0'
            continue
        answer += decoder(int(case[i]))
    
    print(answer)
