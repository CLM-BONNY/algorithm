def solution(a, b):
    a, b = str(a), str(b)
    
    answer = int(a + b) if int(a + b) > 2 * int(a) * int(b) else 2 * int(a) * int(b)
    return answer