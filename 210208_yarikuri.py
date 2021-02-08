for x in range(5):  # 밑의 명령어를 (n)번 반복
    print("Hello, world!")

sum = 0
for x in range(0, 10, 3):  # (n(부터),n(의 -1까지),n(의 간격으로))
    sum = sum + x
print(sum)

for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(x, end="")  # end="">결과를 세로열이 아니고 가로로 한 줄에 출력

for name in ["사순박", "소팔김", "청어김"]:
    print("Hello," + name)

for c in "a,b,c,1,0":
    print(c, end="")  # "__"사이에 있는 모든 문자열을 출력

i = 0
while i < 5:
    print("Hello, world!")
    i = i + 1  # i=0에 1씩 더해서 i의 값이 5보다 커지면 스크립트가 종료되도록 조건을 설정
print("END")

for i in range(1, 100):
    print("for문을 %d번 실행" % i)
    break  # 한번 실행하면 break로 돌아와서 스크립트 종료

sum, i = 0, 0  # 변수 지정
for i in range(1, 101):  # 1부터 100까지 반복해서 실행하지만
    if i % 3 == 0:  # 1부터 100까지의 숫자 중 i의 값이 3으로 나누어 떨어지는(3의 배수) 경우에는
        continue  # 다시 for문으로 돌아가서 재실행
    sum += i
print("1부터 100의 합계(3의 배수 제외):%d" % sum)
