def solution(intStrs, k, s, l):
    answer = []
    
    for num_str in intStrs:
        if int(num_str[s: s+l]) > k:
            answer.append(int(num_str[s: s+l]))
        
    return answer