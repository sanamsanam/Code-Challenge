def game():
    player = []
    win = [['paper', 'rock'], ['rock', 'scissors'], ['scissors', 'paper']]

    print("Lets PLay ROCK_PAPER_SCISSORS")
    print("type you choice :\n  Rock \n  Paper \n  Scissors")
    py1 = input("\nPlayer 1 choose: ")
    py2 = input("\nPlayer 2 choose: ")
    py1 = py1.lower()
    py2 = py2.lower()
    if py1 in ("rock", "paper", "scissors") and py2 in ("rock", "paper", "scissors"):
        if py1 == py2:
            print("Tie")
            return
        else:
            player = [py1, py2]
            for a in win:
                if player == a:
                    print("player 1 win")
                    return
                else:
                    continue
        print("player 2 win")
    else:
        print("\n TYPE CORRECT OPTION")

    return

# MAin Program


ask = "y"
while ask in ("y", "Y", "YES", "Yes", "yes"):
    game()
    ask = input("want to start a new game type y: ")
print("Thank you for playing")
