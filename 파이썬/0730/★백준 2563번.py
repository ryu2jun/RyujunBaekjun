T = int(input())

paper = [[0 for j in range(100)]for i in range(100)]
result = 0
for i in range(T):
    x, y= map(int,input().split())
    for xi in range(x,x+10):
        for yi in range(y,y+10):
            paper[xi][yi] = 1

for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            result += paper[i][j]

print(result)





        

