# import os
# import random
# import time

# # Card arrays
# cardFace = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A']

# userCards = []
# userValue = 0
# dealerCards = []
# dealerValue = 0

# blackJack = True

# bet = 0

# menu = "Enter H - Receive another card.\nEnter P - Keep the cards you have.\nEnter D - Receive your final card and double your bet.\n"

# def playerChoice():

#       global userCards
#       global userValue

#       global bet

#       global dealerValue
#       global dealerCards

#       # Generate user cards

#       # User menu
#       print(menu)

#       time.sleep(1)

#       menuChoice = input()

#       # Hit
#       if menuChoice == "H" or menuChoice == "h":

#          userValue = 0

#          userCards.append(random.choice(cardFace))
         
#          print(f"\nYour cards are:\n{userCards}\n")

#          time.sleep(1)

#          userConvertValue()
#          print(f"Your cards are valued at: {userValue}\n")

#          time.sleep(1)

#          dealer()

#          dealerConvertValue()
         
#       # Double-down
#       elif menuChoice == "D" or menuChoice == "d":
#          userValue = 0

#          userCards.append(random.choice(cardFace))
#          print(f"\nYour cards are:\n{userCards}\n")

#          time.sleep(1)

#          userConvertValue()
#          print(f"Your cards are valued at: {userValue}\n")

#          time.sleep(1)

#          bet = int(bet) + int(bet)
#          print(f"Your current bet is: {bet}\n")

#          time.sleep(1)
         
#          dealerValue = 0
#          dealer()
         

#       # Pass
#       elif menuChoice == "P" or menuChoice == "p":
#          pass

#          dealerValue = 0
#          dealer()

#       else:
#          userValue = 0

# # Dealer action
# def dealer():
#     dealerCards.append(random.choice(cardFace))
   
#     print(f"The dealer has cards:\n{dealerCards}")

#     time.sleep(1)

#     dealerValue = 0
#     dealerConvertValue()
#     print(f"The dealer's cards are valued at {dealerValue}\n")

#     time.sleep(1)

    
#     if userValue == 21:
#          print(f"YOU HIT A BLACKJACK")

#     elif dealerValue == 21:
#          print(f"THE DEALER HIT A BLACKJACK")

#     elif int(userValue) > 21:
#          print(f"YOU BUST")
#          input()
#          TypeError

#     elif int(dealerValue) > 21:
#          print(f"DEALER BUST")
#          input()
#          TypeError

#     elif 21 - int(dealerValue) > 21 - int(userValue):
#         print(f"YOU WIN\nDEALER: {dealerValue}\nYOU: {userValue}\n")

#     elif 21 - int(dealerValue) < 21 - int(userValue):
#         print(f"DEALER WINS\nDEALER: {dealerValue}\nYOU: {userValue}\n")


# # Convert the face value of cards into a value that can be compared (user)
# def userConvertValue():
        
#         global userValue

#         for card in userCards:
#              if card == 'J':
#                 userValue = int(userValue) + 10
#              elif card == 'K':
#                 userValue = int(userValue) + 10
#              elif card == 'Q':
#                 userValue = int(userValue) + 10
#              elif card == 'A':
#                 userValue = int(userValue) + 11
#              else:
#                 userValue = userValue + int(card)

#         for card in userCards:
#             if userValue > 21 and card == 'A':
#                 userValue = int(userValue) - 10

# # Convert the face value of cards into a value that can be compared (dealer)
# def dealerConvertValue():
        
#         global dealerValue

#         for card in dealerCards:
#              if card == 'J':
#                 dealerValue = int(dealerValue) + 10
#              elif card == 'K':
#                 dealerValue = int(dealerValue) + 10
#              elif card == 'Q':
#                 dealerValue = int(dealerValue) + 10
#              elif card == 'A':
#                 dealerValue = int(dealerValue) + 11
#              else:
#                 dealerValue = dealerValue + int(card)

#         for card in dealerCards:
#             if dealerValue > 21 and card == 'A':
#                 dealerValue = int(dealerValue) - 10

# os.system('cls')

# print("-------------------- WELCOME TO BACKJACK --------------------\n")
# time.sleep(1)

# print("What is your bet?:\n")
# bet = input()

# userCards.clear

# userCards.append(random.choice(cardFace))
# userCards.append(random.choice(cardFace))

# dealerCards.append(random.choice(cardFace))

# userConvertValue()
# dealerConvertValue()

# print(f"You have cards:\n{dealerCards}")
# print(f"Your cards are valued at {dealerValue}\n\n")

# print(f"The dealer has cards:\n{dealerCards}")
# print(f"The dealer's cards are valued at {dealerValue}\n")

# while blackJack == True:
#    playerChoice()

