import random
computer_number = random.randrange(1, 101)
user_input = int(input("Enter your Number:-- "))

if user_input > computer_number:
    print("Computer Number: ", computer_number)
    print("Your Guess Number is too High!")
elif user_input < computer_number:
    print("Computer Number: ", computer_number)
    print("Your Guess Number is too Low!")
else:
    print("Computer Number: ", computer_number)
    print("Your Guess Number is too Equal!")
