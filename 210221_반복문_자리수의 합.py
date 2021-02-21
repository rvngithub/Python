sum = 0
origin = int(input("숫자를 입력하세요.>"))  # 1234를 입력받았다고 가정
while origin > 0:
    digit = origin % 10  # digit=4 / digit=3 / digit=2 / digit=1
    sum = sum + digit  # sum=4 / 4+3=7 / 7+2=9 / 9+1=10
    # origin=123 / origin=12 / origin=1 / origin=0이므로 While문에서 빠져나갈 수 있음
    origin = origin // 10
print(sum)  # 결과 출력
# 반복문을 똑똑하게 이용하면 if만 이용한 것보다 더 짧고 간단하게 코드를 짤 수 있다...
