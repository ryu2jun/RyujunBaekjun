
T = int(input())

scores = list(map(int, input().split()))
maxscore = max(scores)
for i in range(T):
    scores[i] = (scores[i]/maxscore*100)

print(sum(scores)/T)