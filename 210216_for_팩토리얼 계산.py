result = 1
req = int(input("어디까지 계산할까요?>"))  # 입력받은 수를 req라는 변수로 지정
for x in range(1, req + 1, 1):
    result = result * x
print(req, "!은 %.1f입니다." % result)  # 결과 출력 %.nf>소수점 자리수를 n만큼 표시
