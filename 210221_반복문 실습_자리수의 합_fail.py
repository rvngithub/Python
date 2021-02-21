origin = int(input("정수를 입력하세요.>"))
if(origin >= 1000):  # 입력받은 숫자가 네자리수라면 (1234)
    a = origin // 1000  # a=1
    b1 = origin % 1000  # b1=234
    if(b1 >= 100):
        b = b1 // 100  # b=2
        c1 = b1 % 100  # c1=34
        if(c1 >= 10):
            c = c1 // 10  # c=3
            d = c1 % 10  # d=4
            print(a + b + c + d)
        elif(c1 > 0):
            c = c1
            print(a + b + c)
        else:
            print(a + b)
    elif(b1 >= 10):
        b = b1 // 10
        c = b1 % 10
        print(a + b + c)
    else:
        b = b1
        print(a + b)
elif(origin >= 100):  # 만약 입력받은 숫자가 세자리수(234?)라면
    a = origin // 100  # a=200
    b1 = origin % 100  # b1=34
    if(b1 >= 10):
        b = b1 // 10  # b=3
        c = b1 % 10  # c=4
        print(a + b + c)
elif(origin >= 10):
    a = origin // 10
    b = origin % 10
    print(a + b)
else:
    a = origin
    print(a)

 # 이 코드는 일단 조건문만 이용했고 반복문을 이용하지 않았다....그리고 몇자리 수를 입력받을 지 모르기 때문에 여러 경우의 수에 대응하기 어려움
