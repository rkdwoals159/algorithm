def solution(n, arr1, arr2):
    answer = ['']*n
    for i in range(n):
        num1 = bin(arr1[i])[2:].rjust(n,'0')
        num2 = bin(arr2[i])[2:].rjust(n,'0')
        for j in range(n):
            if num1[j] == '1' or num2[j] =='1' :
                answer[i] +='#'
            else : answer[i] +=' '
    return answer