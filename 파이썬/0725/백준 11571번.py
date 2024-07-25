
word = input()

word = word.upper()

worddic = {}


for i in word:
    worddic[i] = 0


for i in word:
    for j in worddic.keys():
        if j == i:
            worddic[i] += 1

king = max(worddic.values())
kinglist =[]

for i in worddic.keys():
    if worddic[i] == king:
        kinglist.append(i)

if len(kinglist)> 1:
    print("?")
else:
    print(*kinglist)