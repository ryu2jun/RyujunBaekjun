
while True:
    A, B = map(int, input().split())

    if A == 0 and B== 0:
        break
    else:
        if A // B < 1 and B % A == 0:
            print("factor")
        elif A // B < 1 and B % A != 0:
            print("neither")
        elif A // B >= 1 and A % B == 0:
            print("multiple")
        elif A // B >= 1 and A % B != 0:
            print("neither")
