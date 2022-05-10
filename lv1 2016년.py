def solution(a, b):
    Month = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    Week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    answer = ''
    sum = 0 
    for i in range(1,a) :
        sum += Month[i]
    sum += b
    answer = Week[(sum % 7)-1]
    return answer