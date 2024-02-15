def solution(l, r):
    answer = []
    
    for x in range(l, r+1):
        if all(digit in '05' for digit in str(x)):
            answer.append(x)
        
    if len(answer) == 0:
        answer.append(-1)
        
    return answer