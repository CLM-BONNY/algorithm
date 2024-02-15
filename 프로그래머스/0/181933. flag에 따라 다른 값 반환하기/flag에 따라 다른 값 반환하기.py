def solution(a, b, flag):
    answer = 0
    
    answer = a + b if flag == True else a - b
    
    return answer