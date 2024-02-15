def solution(arr):
    answer = 0
    
    prev_arr = arr
    
    while True:
        curr_arr = []
        for n in prev_arr:
            if n >= 50 and n % 2 == 0:
                curr_arr.append(n // 2)
            elif n < 50 and n % 2 == 1:
                curr_arr.append(n * 2 + 1)
            else:
                curr_arr.append(n)
                
        if prev_arr == curr_arr:
            break
        
        answer += 1
        prev_arr = curr_arr
    
    return answer