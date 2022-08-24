from itertools import count
import random

l = ["Rock", "Scissor", "Paper"]

'''
Rock vs Paper ---> Paper wins
Rock vs Scissor ---> Rock wins
Paper vs Scissor ---> Scissor wins
'''

while True:
    User_Count=0
    Computer_Count=0
    uc = int(input('''
    1 Yes  |  Play
    2 No   | Exit
    '''))

    if uc == 1:
        for a in range(1, 6):
            User_Input = int(input('''
            1 Rock
            2 Scissor
            3 Paper
            '''))
            if User_Input == 1:
                User_Choice = "Rock"
            elif User_Input == 2:
                User_Choice = "Scissor"
            elif User_Input == 3:
                User_Choice = "Paper"
            
            Computer_Choice = random.choice(l)
            print(User_Choice)
            print(Computer_Choice)

            if Computer_Choice == User_Choice:
                print("Computer Value ", Computer_Choice)
                print("User Value ", User_Choice)
                print("Game Draw ")

                User_Count = User_Count + 1
                Computer_Count = Computer_Count + 1

            elif (User_Choice == "Rock" and Computer_Choice == "Scissor") or (User_Choice == "Paper" and Computer_Choice == "Rock") or (User_Choice == "Scissor" and Computer_Choice == "Paper"):
                print("Computer Value ", Computer_Choice)
                print("User Value ", User_Choice)
                print("You Win! ")
                User_Count=User_Count+111

            else:
                print("Computer Value ", Computer_Choice)
                print("User Value ", User_Choice)
                print("Computer Win! ")

                Computer_Count = Computer_Count+1
        
        if User_Count == Computer_Count:
            print("Final Game Draw...")
            print("User Score", User_Count)
            print("Computer Score", Computer_Count)
        elif User_Count > Computer_Count:
            print("Final You Win The Game...")
            print("User Score", User_Count)
            print("Computer Score", Computer_Count)
        else:
            print("Final Computer Win The Game...")
            print("User Score", User_Count)
            print("Computer Score", Computer_Count)
    else:
        break


