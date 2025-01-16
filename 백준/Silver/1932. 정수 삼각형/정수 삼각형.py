# 입력 받기
n = int(input())
triangle = []

for _ in range(n):
    row = list(map(int, input().split()))
    triangle.append(row)

# DP 이용하여 각 위치에서의 최댓값 갱신
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            # 가장 왼쪽인 경우, 위 층의 가장 왼쪽만 더할 수 있음
            triangle[i][j] += triangle[i-1][j]
        elif j == i:
            # 가장 오른쪽인 경우, 위 층의 가장 오른쪽만 더할 수 있음
            triangle[i][j] += triangle[i-1][j-1]
        else:
            # 가운데 있는 경우, 위 층의 j-1, j 중 최댓값 더하기
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

# 출력하기
print(max(triangle[n-1]))
