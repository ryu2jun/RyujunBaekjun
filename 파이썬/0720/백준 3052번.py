

Nlist = []
for i in range(10):
    A = int(input())
    
    if A%42 not in Nlist:
        Nlist.append(A%42)


print(len(Nlist))

