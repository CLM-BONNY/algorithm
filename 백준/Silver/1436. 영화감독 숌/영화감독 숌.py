# 입력 받기
N = int(input())

# N번째 종말의 수 찾기
num = 666
count = 0

while True:
    if '666' in str(num):
        count += 1
    if count == N:
        result = num
        break
    num += 1

# 결과 출력
print(result)
