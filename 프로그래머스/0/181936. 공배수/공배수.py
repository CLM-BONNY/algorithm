def solution(num, n, m):
    answer = 0
    
    answer = 1 if num % n == 0 and num % m == 0 else 0
    
    return answer