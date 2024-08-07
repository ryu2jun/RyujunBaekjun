total = int(input())

type = int(input())

real = 0
for i in range(1,type+1):
    much, many = map(int, input().split())
    real += much*many
print(real)
if total == real:
    print("Yes")
    
else:
    print("No")