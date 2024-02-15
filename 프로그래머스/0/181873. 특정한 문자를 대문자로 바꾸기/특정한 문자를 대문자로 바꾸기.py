def solution(my_string, alp):
    answer = ''
    
    for s in my_string:
        answer += s.upper() if s == alp else s

    return answer