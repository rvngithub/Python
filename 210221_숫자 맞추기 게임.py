import random
# 1부터 100까지의 숫자 중에서 랜덤으로 고름. 이것이 플레이어가 맞춰야 하는 정답
ans = random.randrange(1, 101)
count = 0  # 나중에 정답을 맞춘 뒤 시도 회수를 알려줄 변수
print("1부터 100 사이의 숫자를 맞추시오. 총 기회는 10번 입니다.")
while count < 10:  # 역시 while문은 최대 횟수를 정해놓고 가야하는건가? 조건이 참인 "동안" 실행하는 거라서?
    player = int(input("1부터 100 사이의 숫자를 맞추시오.>"))
    count = count + 1
    if player > ans:
        print("정답보다 높습니다!")
        continue
    elif player < ans:
        print("정답보다 낮습니다!")
    else:
        break
if player == ans:
    print("정답입니다. 총 %d번만에 맞추셨습니다." % count)
else:
    print("정답은", ans, "이었습니다.")
