def solution(my_string, queries):
    answer = list(my_string)
    
    for x in range(len(queries)):
        s = queries[x][0]
        e = queries[x][1]
        
        
        sub_string = answer[s:e+1][:: -1]
        answer[s:e+1] = sub_string
        
    answer = ''.join(answer)
    
    return answer