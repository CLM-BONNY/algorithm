def solution(a, d, included):
    answer = 0
    currentNum = a
    
    for i in range(len(included)):
        if included[i]:
            answer += currentNum
        currentNum += d
        
    return answer