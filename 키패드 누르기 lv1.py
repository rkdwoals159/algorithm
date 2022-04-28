def solution(numbers, hand):
    answer = ''
    left = [3,0]
    right = [3,2]
    
    for i in numbers :
        if i != 0:
            num = [(i-1)//3,(i-1)%3]
        else : num = [3,1]
        
        if num[1] == 0:
            answer +='L'
            left = num
        elif num[1] == 2:
            answer +='R'
            right = num
        else:
        
            if abs(num[0]-left[0]) +  abs(num[1]-left[1]) > abs(num[0]-right[0]) +  abs(num[1]-right[1]) :
                answer += 'R'
                right = num
            elif abs(num[0]-left[0]) +  abs(num[1]-left[1]) == abs(num[0]-right[0]) +  abs(num[1]-right[1]) :
                if hand == 'left':
                    answer += 'L'
                    left = num
                else :
                    answer += 'R'
                    right = num
            else :
                answer +='L'
                left = num
                
    

    return answer