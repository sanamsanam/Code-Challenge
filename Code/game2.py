# with computer player
import random
ask = "y"
option = [1, 2, 3]
while ask in ("y", "Y", "YES", "Yes", "yes"):
    print("\nLets PLay ROCK_PAPER_SCISSORS\n")
    print("*****************************")
    print("Enter you choice :\n 1: Rock \n 2: Paper \n 3: Scissors")
    py = int(input("\nPlayer 1 choose: "))
    com = random.choice(option)
    print(f"Computer choose:{com}")

    if py == com:
        print("\n*****************************\n")
        print("Its a tie")
        print("\n*****************************\n")
    elif (com == 1) and (py == 3) or (com == 3) and (py == 2) or (com == 2) and (py == 1):
        print("\n*****************************\n")
        print("Computer Wins")
        print("\n*****************************\n")
    else:
        print("\n*****************************\n")
        print(" Cong: Player Win")
        print("\n*****************************\n")
    ask = input("want to start a new game y/n: ")
print("\n*****************************\n")
print("Thank you for playing")
print("\n*****************************\n")

# computer win logig  rock scissors  1,3    scissors Paper   3,2    paper rock 2,1
