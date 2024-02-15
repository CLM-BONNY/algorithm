def solution(my_string, m, c):
    answer = ''
    
    for i in range(int(len(my_string)/m)):
        answer += my_string[c+m*i-1]
    
    return answer