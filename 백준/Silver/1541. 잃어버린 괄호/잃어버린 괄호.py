# 입력받기
expression = input()

# '-'를 기준으로 식을 나누기
parts = expression.split('-')

# 첫 번째 부분(무조건 더하기)
result = sum(map(int, parts[0].split('+')))

# 나머지 부분(전부 더한 후 빼기)
for part in parts[1:]:
    result -= sum(map(int, part.split('+')))

# 결과 출력하기
print(result)
