def solution(numbers):
    numbers.sort(key=lambda x: str(x) * 3, reverse=True)
    
    answer = ''.join(str(x) for x in numbers)
    return answer if answer[0] != "0" else "0"