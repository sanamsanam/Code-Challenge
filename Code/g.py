# rock paper scissors game with computer player
import random
ask = "y"
option = ["rock", "paper", "scissors"]
while ask in ("y", "Y", "YES", "Yes", "yes"):
    print("\nLets PLay ROCK_PAPER_SCISSORS\n")
    print("*****************************")
    print("Enter you choice :\n : Rock \n : Paper \n : Scissors")
    py = (input("\nPlayer 1 choose: ").lower())
    com = random.choice(option).lower()
    print(f"Computer choose: {com}")

    if py == com:
        print("\n*****************************\n")
        print("Its a tie")
        print("\n*****************************\n")
    # computer win  rock scissors  1,3    scissors Paper   3,2    paper rock 2,1
    elif (com == "rock") and (py == "scissors") or (com == "scissors") and (py == "paper") or (com == "paper") and (py == "rock"):
        print("\n*****************************\n")
        print("Computer Wins")
        print("\n*****************************\n")
    else:
        print("\n*****************************\n")
        print(" Congratulation: Player Win")
        print("\n*****************************\n")
    ask = input("Want to start a new game y/n: ")
print("\n*****************************\n")
print("Thank you for playing")
print("\n*****************************\n")
