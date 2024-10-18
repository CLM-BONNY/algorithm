import sys

# 입력 받기
input = sys.stdin.read
data = input().splitlines()

# 첫 번째 줄에서 N(저장된 사이트의 수)과 M(찾으려는 사이트의 수)를 분리
n, m = map(int, data[0].split())

# 딕셔너리 생성
site_passwords = {}

# 사이트 주소와 비밀번호 입력 받기
for i in range(1, n+1):
    site, password = data[i].split()
    site_passwords[site] = password

# 비밀번호를 찾으려는 사이트 주소에 대해 비밀번호 출력
output = []
for i in range(n+1, n+1+m):
    site = data[i]
    output.append(site_passwords[site])

# 결과 출력
sys.stdout.write("\n".join(output) + "\n")
