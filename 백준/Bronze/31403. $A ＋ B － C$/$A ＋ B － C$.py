import sys

# 입력 받기
A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

# 출력
print(A + B - C)
print(int(str(A) + str(B)) - C)
