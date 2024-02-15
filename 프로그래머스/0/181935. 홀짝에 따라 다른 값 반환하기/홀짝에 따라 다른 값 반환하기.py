def solution(n):
    answer = 0
    
    if n % 2 != 0:
        for num in range(1, n+1, 2):
            answer += num
    else:
        for num in range(0, n+1, 2):
            answer += pow(num, 2)
    
    return answer