def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: x*10, reverse=True)
    
    return str(int(''.join(numbers)))