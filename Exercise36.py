
def pickanumber():
    print("What number am I thinking of? (1-9)")

    choice = input("> ")
    if "0" in choice:
        print("I said a number from 1 to 9")
    else:
        print("Type your number in again, I forgot it already.")
    choice = input("> ")
    chosennumber = int(choice)

    choice2 = input("try again > ")
    if chosennumber == 7:
        print("Good job! You win!")
    if chosennumber == 6 or chosennumber == 8:
        print("You're so close! I'll give you another try.")      
    choice2 = input("try again > ")
    chosennumber2 = int(choice2)

    if chosennumber2 == 7:
        print("You win! See, I told you you were close! Well done!")
    elif chosennumber != 7:
        print("You sure are bad at this game! You lose.")

pickanumber()
    


    
