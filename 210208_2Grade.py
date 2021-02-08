ID = input("Please input your ID>")
math = int(input("Please input your Math score>"))
eng = int(input("Please input your English score>"))
if (math + eng) / 2 >= 90:
    print("Your grade is A")
elif(math + eng) / 2 >= 80:
    print("Your grade is B")
elif(math + eng) / 2 >= 70:
    print("Your grade is C")
elif(math + eng) / 2 >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")
