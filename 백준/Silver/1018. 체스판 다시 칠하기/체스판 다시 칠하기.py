# 입력 받기
N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 최소 다시 칠해야 하는 정사각형 개수 계산
pattern1 = ['WBWBWBWB', 'BWBWBWBW'] * 4
pattern2 = ['BWBWBWBW', 'WBWBWBWB'] * 4

min_changes = float('inf')

for start_i in range(N - 7):
    for start_j in range(M - 7):
        changes1 = 0
        changes2 = 0

        for i in range(8):
            for j in range(8):
                if board[start_i + i][start_j + j] != pattern1[i][j]:
                    changes1 += 1
                if board[start_i + i][start_j + j] != pattern2[i][j]:
                    changes2 += 1

        min_changes = min(min_changes, changes1, changes2)

# 결과 출력
print(min_changes)