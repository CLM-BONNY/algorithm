import sys

N, M = map(int, sys.stdin.readline().split())

pkm_int_key = {}
pkm_name_key = {}
for i in range(N):
    name = sys.stdin.readline().strip()
    pkm_int_key[i] = name
    pkm_name_key[name] = i

for j in range(M):
    question = sys.stdin.readline().strip()
    if question.isdigit():
        print(pkm_int_key[int(question)-1])
    else:
        print(pkm_name_key[question]+1)
