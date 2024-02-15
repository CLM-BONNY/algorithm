def solution(arr, queries):
    answer = arr
    
    for x in range(len(queries)):
        s = queries[x][0]
        e = queries[x][1]
        
        for i in range(s, e+1):
            answer[i] += 1
    
    return answer