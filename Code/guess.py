import random
print("\n*******************\n")
print("Let play a Guessing Game 1-9")
print("\n*******************\n")
choice = ""
no = random.randint(1, 9)
while choice != "exit":
    user = int(input("Guess a no: "))

    if user > no:
        print("\n*******************\n")
        print("you guessed to High")
        print("\n*******************\n")
    elif user < no:
        print("\n*******************\n")
        print("you guessed to Low")
        print("\n*******************\n")
    else:
        print("\n*******************\n")
        print("Congratulation! you guessed Correct")
        print("\n*******************\n")
        break
    choice = input("do you want to Continue: ")


print("Thanks for Playing")
print("\n*******************\n")
