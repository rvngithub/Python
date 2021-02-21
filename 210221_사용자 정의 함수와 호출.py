def add(a, b):  # 이 코드에서 쓸 함수를 처음에 정의하고 시작. 이 점은 C언어와 똑같음
    return a + b


def swap(a, b):
    a, b = b, a
    return a, b


print("사용자 정의 함수를 만들고 그 함수를 호출하는 실습입니다.")
a = int(input("첫번째 스코어를 입력>"))
b = int(input("두번째 스코어를 입력>"))
sum = add(a, b)
avg = sum / 2
print("두 점수의 합:", sum)
print("두 정수의 평균:", avg)
a, b = swap(a, b)
print("두 점수의 순서를 그냥 바꿔보았음:", a, b)
