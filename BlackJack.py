import os
import random
import time

# Card arrays
cardFace = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A']

userCards = []
userValue = 0
dealerCards = []
dealerValue = 0

bet = 0

def playerChoice():

    global userCards
    global userValue
    global bet

    # Generate user cards
    userCards.append(random.choice(cardFace))
    userCards.append(random.choice(cardFace))

    print(f"\nYour cards are:\n{userCards}\n")

    userConvertValue()
    print(f"Your cards are valued at: {userValue}\n")


    # User menu
    print("Enter H - Receive another card.\nEnter P - Keep the cards you have.\nEnter D - Receive your final card and double your bet.")
    menuChoice = input()

    # Hit
    if menuChoice == "H" or menuChoice == "h":

        userValue = 0

        userCards.append(random.choice(cardFace))
        print(f"\nYour cards are:\n{userCards}\n")

        userConvertValue()
        print(f"Your cards are valued at: {userValue}\n")

    # Pass
    elif menuChoice == "P" or menuChoice == "P":
        pass
        # dealer plays

    # Double-down
    elif menuChoice == "D" or menuChoice == "d":

        userValue = 0

        userCards.append(random.choice(cardFace))
        print(f"\nYour cards are:\n{userCards}\n")

        bet = int(bet) + int(bet)

        userConvertValue()
        print(f"Your cards are valued at: {userValue}\n")

    else:
        userValue = 0

        playerChoice()



    playerChoice()

def dealer():
    dealerCards.append(random.choice(cardFace))
    dealerCards.append(random.choice(cardFace))

    dealerConvertValue()

    print(f"The dealer has cards:\n{dealerCards}")
    print(f"The dealer's cards are valued at {dealerValue}")


# Convert the face value of cards into a value that can be compared (user)
def userConvertValue():
        
        global userValue

        for card in userCards:
             if card == 'J':
                userValue = int(userValue) + 10
             elif card == 'K':
                userValue = int(userValue) + 10
             elif card == 'Q':
                userValue = int(userValue) + 10
             elif card == 'A':
                userValue = int(userValue) + 11
             else:
                userValue = userValue + int(card)

        for card in userCards:
            if userValue > 21 and card == 'A':
                userValue = int(userValue) - 10

# Convert the face value of cards into a value that can be compared (dealer)
def dealerConvertValue():
        
        global dealerValue

        for card in dealerCards:
             if card == 'J':
                dealerValue = int(dealerValue) + 10
             elif card == 'K':
                dealerValue = int(dealerValue) + 10
             elif card == 'Q':
                dealerValue = int(dealerValue) + 10
             elif card == 'A':
                dealerValue = int(dealerValue) + 11
                if dealerValue > 21:
                    dealerValue = dealerValue - 10
             else:
                dealerValue = dealerValue + int(card)

os.system('cls')

print("-------------------- WELCOME TO BACKJACK --------------------\n")
time.sleep(1)

print("What is your bet?:\n")
bet = input()
playerChoice()
