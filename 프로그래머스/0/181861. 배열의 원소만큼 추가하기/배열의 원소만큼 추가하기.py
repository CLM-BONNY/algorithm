def solution(arr):
    answer = []
    
    for n in arr:
        answer += [n for i in range(n)]
    
    return answer