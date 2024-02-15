def solution(arr, queries):
    answer = [0 for j in range(len(queries))]
    
    for x in range(len(queries)):
        s = queries[x][0]
        e = queries[x][1]
        k = queries[x][2]
        
        num_min = float("inf") 
        for i in range(s, e+1):
            if arr[i] > k and arr[i] < num_min:
                num_min = arr[i]
        if num_min == float("inf"):
            num_min = -1
            
        answer[x] = num_min
                
    return answer