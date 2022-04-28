def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0 :
                continue
            else :
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
        
        if len(stack)>1 :
            if stack[-1] == stack[-2] :
                stack.pop()
                stack.pop()
                answer +=2
    
    return answer