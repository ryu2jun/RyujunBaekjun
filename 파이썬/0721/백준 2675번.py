T = int(input())
result =''
for i in range(T):
    N, A = input().split()
    for j in range(0,len(A)):
        result += A[j]*int(N)
    
    print(result)
    result = ''
