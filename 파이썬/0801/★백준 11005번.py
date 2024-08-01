
N, B = map(int, input().split())

NUM = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''
while N: # N이 0이 될때까지
    result += str(NUM[N%B]) #결과에 N을 36으로 나눈 나머지의 문자열을 더함
    N //= B #N을 B로 나눈 몫으로 초기화

print(result[::-1]) # 문자열을 반대로 프린트

