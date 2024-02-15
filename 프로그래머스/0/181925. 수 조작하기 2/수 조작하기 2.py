def solution(numLog):
    answer = ''
    prev_num = numLog[0]
    
    for i in range(1, len(numLog)):
        if prev_num + 1 == numLog[i]:
            answer += 'w'
        elif prev_num - 1 == numLog[i]:
            answer += 's'
        elif prev_num + 10 == numLog[i]:
            answer += 'd'
        else:
            answer += 'a'
        prev_num = numLog[i]
    return answer