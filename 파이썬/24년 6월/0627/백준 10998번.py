# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# map 함수 사용하기

# map 함수는 반복적인 작업을 수행할때 좋음
A, B = map(int, input().split())

print(A*B)
