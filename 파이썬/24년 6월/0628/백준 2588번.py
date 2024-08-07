A = int(input())
B = int(input())

print(A*(B%10))

#두번째 수의 1의 자리 나머지 곱하기 

print(round(A*((B-B%10)%100)/10))

#두번째 수의 10의 자리 나머지 곱하기 

print(round((A*((B-B%100)))/100))

#두번째 수의 100의 자리 나머지 곱하기 

print(A*B)