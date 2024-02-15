def solution(start, end_num):
    answer = []
    
    for x in range(start, end_num-1, -1):
        answer.append(x)
    
    return answer