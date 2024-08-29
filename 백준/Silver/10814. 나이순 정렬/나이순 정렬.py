import sys

# 입력 받기
n = int(sys.stdin.readline().strip())

people = []

for i in range(n):
  age, name = sys.stdin.readline().strip().split()
  age = int(age)
  people.append((age, name, i))  # (나이, 이름, 가입 순서)

# 나이 오름차순으로 정렬하되, 나이가 같으면 가입 순서(i)를 기준으로 정렬
people.sort(key=lambda x: (x[0], x[2]))

# 결과 출력
for person in people:
  print(person[0], person[1])