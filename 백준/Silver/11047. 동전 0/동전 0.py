# 입력 받기
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# 동전 내림차순 정렬
coins.sort(reverse=True)

count = 0

for coin in coins:
  if K == 0:
    break
  count += K // coin # 해당 동전을 최대한 많이 사용
  K %= coin # 남은 금액 갱신

print(count)