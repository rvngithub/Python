names = []

while True:
    name = input("학생 이름을 입력하세요.>")
    names.append(name)
    if name == "":
        break

print("학생 이름:")
for name in names:
    print(name, end=',')
