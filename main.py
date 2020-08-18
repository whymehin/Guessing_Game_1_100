from math import *
import random

again=True
print("Random number guessing game (1-100): ")
while again:
    min = 1
    max = 100
    bingo = random.randint(1, 100)
    ans=input("Show answer? Y/N: ")
    if ans.lower()=="y":
        print(bingo)
    elif ans.lower()=="n":
        print("Good Luck")
    else:
        print("Invalid Input")

    guess = ""
    test = ""
    check=True
    while bingo!=guess and check:
        print("The answer is between " + str(min) + " and " + str(max))
        guess = input("Tell me your guess: ")
        if guess.isnumeric():
            guess=int(guess)
            if guess> min and guess< max:
                if guess< bingo:
                    min=guess
                elif guess>bingo:
                    max=guess
                elif guess==bingo:
                    print("BINGO")
                    test=input("Continue: Y/N? ")
                    if test.upper() == "Y":
                        again=True
                    elif test.upper() == "N":
                        again=False
                        print("BYE BYE")
                    else:
                        print("ERROR")
                        again=False
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")






