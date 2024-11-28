# 입력 받기
total = int(input())
results = []

for _ in range(total):
    n = int(input())
    
    if n == 0:  # 의상이 없는 경우
        results.append(0)
        continue
    
    clothes_dict = {}
    for _ in range(n):
        name, kind = input().split()
        if kind not in clothes_dict:
            clothes_dict[kind] = 0
        clothes_dict[kind] += 1
    
    combinations = 1
    for count in clothes_dict.values():
        combinations *= (count + 1)  # 입는 경우와 입지 않는 경우 포함
    
    results.append(combinations - 1)  # 알몸인 경우 제외

# 결과 출력
for result in results:
    print(result)
