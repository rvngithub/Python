a = 10
b = 20
sum = a + b
# 변수를 정할 때 C언어와는 달리 변수의 데이터 타입을 지정하지 않아도 됨 int형, float형, char 등....
print(a, "+", b, "=", sum)

x = 10
y = 20
x, y = y, x  # Python에선 변수끼리 swap을 이와 같은 코드로 간단하게 할 수 있음
print(x, y)
