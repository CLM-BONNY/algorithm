word = list(input().upper())
for x in word:
    x.upper()
unique = list(set(word))

cnt_number = []
for y in unique:
    cnt = word.count(y)
    cnt_number.append(cnt)

if cnt_number.count(max(cnt_number)) > 1:
    print("?")
else:
    max_index = cnt_number.index(max(cnt_number))
    print(unique[max_index])