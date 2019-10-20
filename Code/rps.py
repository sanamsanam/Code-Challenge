
ask = "y"
while ask in ("y", "Y", "YES", "Yes", "yes"):
    print("Lets PLay ROCK_PAPER_SCISSORS")
    print("Enter you choice :\n 1: Rock \n 2: Paper \n 3: Scissors")
    py1 = int(input("\nPlayer 1 choose: "))
    py2 = int(input("\nPlayer 2 choose: "))
    if py1 == py2:
        print("Its a tie")
    elif (py1 == 1) and (py2 == 2) or (py1 == 3) and (py2 == 1) or (py1 == 3) and (py2 == 2):
        print("Congratulation! Player 2 wins")
    elif (py2 == 1) and (py1 == 2) or (py2 == 3) and (py1 == 1) or (py2 == 3) and (py1 == 2):
        print("Congratulation! Player 1 wins")
    ask = input("want to start a new game y/n: ")

print("Thank you for playing")
