from random import randint as rn

print("Hello There!")
question = input("Would you like to play a game of 'Rock, Paper, Scissoors' with me? [y/n] ")

while question.lower() != 'n':
    if question.lower() == 'y':
        randomNumber = rn(1, 3)

        choice = input("What do you choose, Rock, Paper or Scissors? [r/p/s] ")

        if choice.lower() == 'r' and randomNumber == 1:
            print("I have chosen rock. We have chosen the same thing.")
            question = input("Would you like to play again? [y/n] ")
        elif choice.lower() == 'r' and randomNumber == 2:
            print("I have chosen paper. You lost!")
            question = input("Would you like to play again? [y/n] ")
        elif choice.lower() == 'r' and randomNumber == 3:
            print("I have chosen scissors. You won!")
            question = input("Would you like to play again? [y/n] ")

        elif choice.lower() == 'p' and randomNumber == 1:
            print("I have chosen rock. You won!")
            question = input("Would you like to play again? [y/n] ")
        elif choice.lower() == 'p' and randomNumber == 2:
            print("I have chosen paper. We have chosen the same thing")
            question = input("Would you like to play again? [y/n] ")
        elif choice.lower() == 'p' and randomNumber == 3:
            print("I have chosen scissors. You lost!")
            question = input("Would you like to play again? [y/n] ")


        elif choice.lower() == 's' and randomNumber == 1:
            print("I have chosen rock. You lost!")
            question = input("Would you like to play again? [y/n] ")
        elif choice.lower() == 's' and randomNumber == 2:
            print("I have chosen paper. You won!")
            question = input("Would you like to play again? [y/n] ")
        elif choice.lower() == 's' and randomNumber == 3:
            print("I have chosen scissors. We have chosen the same thing.")
            question = input("Would you like to play again? [y/n] ")

        else:
            print("Invalid input. Please type 'r', 'p', 's'")

    else:
        print("Invalid input. Please type 'y' or 'n'")
        question = input("Would you play again? [y/n] ")

print("Good-bye!")
