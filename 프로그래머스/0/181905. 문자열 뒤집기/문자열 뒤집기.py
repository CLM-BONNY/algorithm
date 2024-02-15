def solution(my_string, s, e):
    sub_string = my_string[s:e+1]
    
    answer = my_string[:s] + sub_string[::-1] + my_string[e+1:]
    
    
    return answer