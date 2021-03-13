score_list = []  # 전체 점수의 평균을 구하기 위한 리스트
over80_list = []  # 과 80점 이상의 점수를 받은 학생의 갯수만 세기 위해 리스트를 따로 만든다


def calc(score_list, b):  # 리스트 안의 점수들 평균 계산하는 함수
    total = sum(score_list)  # 리스트 내의 모든 합을 구할 경우 쓸 수 있다
    result = total / b
    return result


a = 0  # 점수를 입력받을 변수
b = int(input("학생 수를 입력하세요>"))  # 학생이 총 몇명이 될 지 사전엔 모른다는 가정 하에 학생 수를 입력받음
for x in range(b):  # 입력 받은 학생 수만큼 아래의 코드를 반복
    a = int(input("성적을 입력하세요>"))
    score_list.append(a)  # 입력받은 점수를 일단 전체 점수 리스트에 넣는다
    if a >= 80:
        over80_list.append(a)  # 그리고 입력받은 점수가 80보다 높거나 같다면 80점 이상의 리스트에 넣는다
avg = calc(score_list, b)  # 위에서 작성한 평균을 구해주는 calc 함수 호출
print("성적 평균은", avg, "입니다.")
print("80점 이상 성적을 받은 학생 수는", len(over80_list), "명 입니다.")
