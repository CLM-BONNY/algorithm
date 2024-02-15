def solution(my_strings, parts):
    answer = ''
    
    for x in range(len(parts)):
        s = parts[x][0]
        e = parts[x][1]
        
        answer += my_strings[x][s: e+1]
        
    return answer