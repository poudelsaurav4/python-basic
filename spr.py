import random

win_countuser = 0 
win_countcomputer = 0
for i in range(3):
    random_num = random.randint(1,3)
    user_inp = int(input("enter 1 for rock,2 for sissor,3 for rock "))

    if user_inp ==1:
        print("rock")
    elif user_inp ==2:
        print("Sissor")
    elif user_inp ==3:
        print("paper")
    else:
        print("enter a valid number")

    print(random_num)

    if random_num ==1:
        print("rock")
    elif random_num ==2:
        print("Sissor")
    else:
        print("paper")


    if user_inp == random_num:
        print(f" it is draw, score is {win_countuser}: {win_countcomputer}")
        win_countuser+=0
        win_countcomputer+=0

    elif user_inp == 1 and random_num==2:
        win_countuser+=1
        win_countcomputer+=0
        print(f"user wins {win_countuser}: {win_countcomputer}")
        

    elif user_inp == 2 and random_num == 3:
        win_countuser+=1
        win_countcomputer+=0
        print(f"user wins, {win_countuser}: {win_countcomputer}")
        


    elif user_inp > random_num:
        win_countuser+=0
        win_countcomputer+=1
        print(f"computer wins {win_countuser}: {win_countcomputer}")
        

    else:
        win_countcomputer+=1
        win_countuser+=0
        print(f"computer wins {win_countuser}: {win_countcomputer}")
        
if win_countcomputer> win_countuser:
    print(f"computer won with score{win_countcomputer}:{win_countuser}", )
elif win_countuser> win_countcomputer:
    print(f"user won with score {win_countuser}:{win_countcomputer}")
else:
    print(f"its draw {win_countcomputer}:{win_countuser}")

