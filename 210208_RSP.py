import random
P1 = input("Select R, S, P>")
rsp = ['R', 'S', 'P']
PC = random.choice(rsp)
print("You choose", P1, "PC choose", PC)
if(P1 == 'R') and (PC == 'P'):
    print("You lose!")
elif(P1 == 'R') and (PC == 'S'):
    print("You win!")
elif(P1 == 'S') and (PC == 'R'):
    print("You lose!")
elif(P1 == 'S') and (PC == 'P'):
    print("You win!")
elif(P1 == 'P') and (PC == 'S'):
    print("You lose!")
elif(P1 == 'P') and (PC == 'R'):
    print("You win!")
else:
    print("DRAW")
