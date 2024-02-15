def solution(n, k):
    answer = []
    
    for x in range(1, n+1):
        if x % k == 0:
            answer.append(x)
    
    return answer