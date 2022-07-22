N = int(input())

words = set()
for i in range(N):
    word = input()
    words.add(word)

answer = list(words)

answer.sort(key=lambda x: (len(x), x))

for j in answer:
    print(j)