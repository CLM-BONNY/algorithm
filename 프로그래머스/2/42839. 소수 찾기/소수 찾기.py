from itertools import permutations

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True
        
    
def solution(numbers):
    answer = 0
    
    num_list = list(numbers)
    
    all_permutations = set()
                   
    for length in range(1, len(num_list) + 1):
        all_permutations.update(permutations(num_list, length))
    
    new_numbers = set(int(''.join(perm)) for perm in all_permutations)
    
    for n in new_numbers:
        if is_prime(n):
            answer += 1
        
    return answer