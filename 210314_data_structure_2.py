list_of_friends = []  # 친구 목록을 저장하기 위한 빈 리스트


def hello_my_friend(list_of_friends, new_friend):
    if new_friend not in list_of_friends:
        return new_friend
    else:
        while new_friend in list_of_friends:
            new_friend = input("이미 존재하는 이름입니다! 다시 입력해주세요>")
            if new_friend not in list_of_friends:
                return new_friend
            else:
                continue


def check(list_of_friends, old_name):  # 입력받은 이름이 리스트 안에 존재하는지 체크하는 함수
    if old_name in list_of_friends:
        return old_name
    else:
        while old_name not in list_of_friends:
            old_name = input("해당 이름은 존재하지 않습니다. 다시 입력해주세요>")
            if old_name in list_of_friends:
                return old_name
            else:
                continue


def serch(list_of_friends, checked):  # 입력된 이름의 주소를 찾아주는 함수
    adress = list_of_friends.index(checked)
    return adress


def replace(list_of_friends, adress, new_name):  # 사전에 입력된 이름의 주소에 다른 이름을 넣어주는 함수(이름변경)
    del(list_of_friends[adress])
    list_of_friends.insert(adress, new_name)
    return


while True:
    print("\n1.친구 리스트 출력\n2.친구 추가\n3.친구 삭제\n4.이름 변경\n9.종료\n")
    menu_select = int(input("메뉴를 선택하시오>"))
    if menu_select == 9:
        break
    elif menu_select == 1:
        print(list_of_friends, sep="\n")
    elif menu_select == 2:
        new_friend = input("이름을 입력하세요>")
        add_name = hello_my_friend(list_of_friends, new_friend)
        list_of_friends.append(add_name)
        print("추가가 완료되었습니다.")
    elif menu_select == 3:
        old_name = input("삭제하고 싶은 친구의 이름을 입력하세요>")
        checked = check(list_of_friends, old_name)
        adress = serch(list_of_friends, checked)
        del(list_of_friends[adress])
        print("삭제가 완료되었습니다.")
    elif menu_select == 4:
        old_name = input("변경하고 싶은 친구의 이름을 입력하세요>")
        checked = check(list_of_friends, old_name)
        adress = serch(list_of_friends, checked)
        new_name = input("변경된 이름을 입력하세요>")
        change = replace(list_of_friends, adress, new_name)
        print("변경이 완료되었습니다.")
    else:
        print("해당 기능은 존재하지 않습니다. 번호를 확인 후 다시 입력해주세요!")
        continue
