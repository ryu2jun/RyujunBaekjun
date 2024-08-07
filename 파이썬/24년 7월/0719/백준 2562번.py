Nlist =[]
for i in range(1,10):
    Nlist.append(int(input()))



print(max(Nlist))
print(Nlist.index(max(Nlist))+1)