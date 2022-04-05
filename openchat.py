answer = []
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
user = {} #{uid : nickname} 딕셔너리로 관리
access_list = [] #[uid 출입 할때마다 추가 1,uid1234,0,uid1234]
for i in record : 
    i = i.split()
    if i[0] == 'Enter' : 
        user[i[1]] = i[2]
        access_list.append(1)
        access_list.append(i[1])
    elif i[0] == 'Change' : 
        user[i[1]] = i[2]
    else : 
        access_list.append(0)
        access_list.append(i[1])
        
for j in range(int(len(access_list)/2)) :
    if access_list[2*j] == 1 :
        temp = access_list[2*j+1]
        answer.append(str(user[temp])+'님이 들어왔습니다.')
    else : 
        temp = access_list[2*j+1]
        answer.append(str(user[temp])+'님이 나갔습니다.')
print(answer)