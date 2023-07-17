import os
import random
import time

tCards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A']

uCards = []
dCards = []

uValue = 0
dValue = 0

allowBet = True
bet = 0
def menu(bet):

    
    print("\nH -> Hit\nD -> Double-down\nS -> Stay\n")
    play = input()

    if play == "H" or play == "h":
        uCards.append(random.choice(tCards))
        check()
        pass

    elif play == "D" or play == "d":
        bet = int(bet) + int(bet) 
        print(f"Your new bet is {bet}.")
        uCards.append(random.choice(tCards))
        print(f"{uCards}")

        check()
        pass

    elif play == "S" or play == "s":
        dCards.remove("~")
        while int(dValue) <= 17:
            dCards.append(random.choice(tCards))
            check()
        pass

def uEval():

    global uValue

    uValue = 0

    for i in uCards:
        if i == 'J':
            uValue = int(uValue) + 10
        elif i == 'K':
            uValue = int(uValue) + 10
        elif i == 'Q':
            uValue = int(uValue) + 10
        elif i == 'A':
            uValue = int(uValue) + 11
        else:
            uValue = int(i) + uValue

    for i in uCards:
        if uValue > 21 and i == 'A':
            uValue = int(uValue) - 10
    
    print(uCards)
    time.sleep(.5)
    print(f"YOU: {uValue}.")

def dEval():

    global dValue

    dValue = 0

    for i in dCards:
        if i == '~':
            dValue = int(dValue) + 0
        elif i == 'J':
            dValue = int(dValue) + 10
        elif i == 'K':
            dValue = int(dValue) + 10
        elif i == 'Q':
            dValue = int(dValue) + 10
        elif i == 'A':
            dValue = int(dValue) + 11
        else:
            dValue = int(i) + dValue

    for i in dCards:
        if dValue > 21 and i == 'A':
            dValue = int(dValue) - 10

    print(dCards)
    time.sleep(.5)
    print(f"DEALER: {dValue}.")

def check():

    global bet
    
    print("")
    uEval()
    print("")
    time.sleep(.5)
    dEval()

    if int(uValue) > 21:
        time.sleep(.5)
        print("\nYOU BUSTED!\n")
        walletLoss(bet)
        pass
    elif int(dValue) > 21:
        time.sleep(.5)
        print("\nDEALER BUSTED!\n")
        walletWin(bet)
        pass
    elif int(uValue) == 21:
        time.sleep(.5)
        print("\nBLACKJACK!\n")
        walletWin(bet)
        pass
    elif int(dValue) == 21:
        time.sleep(.5)
        print("\nDEALER BLACKJACK!\n")
        walletLoss(bet)
        pass
    elif int(dValue) >= 17 and int(dValue) >= int(uValue):
        time.sleep(.5)
        print("\nYOU LOSE!\n")
        walletLoss(bet)
        pass
    elif int(uValue) >= 17 and int(dValue) >= 17 and int(uValue) > int(dValue):
        time.sleep(.5)
        print("\nYOU WIN!\n")
        walletWin(bet)
        pass
    elif int(uValue) >= 17 and int(dValue) >= 17 and int(dValue) > int(uValue):
        time.sleep(.5)
        print("\nYOU LOSE!\n")
        walletLoss(bet)
        pass
    else:
        time.sleep(.5)
        pass

def walletRead():

    global allowBet

    while allowBet == True:
        with open('balance.txt', 'r') as docRead:
            docRead = docRead.read()

            if int(docRead) <= 0:
                bet = 1
                return bet

            print(f"Your balance is: {int(docRead)}.\nHow much would you like to bet?:")
            bet = input()

            if int(docRead) >= int(bet) and int(bet) >= 0:
                allowBet = True
                return bet
            else:
                allowBet == False
                os.system('cls')
                print(f"You cannot bet {int(bet)} as you only have {docRead}.")
        
def walletWin(bet):

    with open('balance.txt', 'r') as file:
        balance = file.read()
        file.read = balance
        newBal = int(bet) + int(balance)

        if newBal == 0 or newBal < 0:
            newBal == 1

    with open('balance.txt', 'w') as docWrite:
        docWrite.write(str(newBal))
        print(f"Bet: {bet}\nNew balance: {newBal}\n")
        wait()

def walletLoss(bet):
    
    with open('balance.txt', 'r') as file:
        balance = file.read()
        file.read = balance
        newBal = -int(bet) + int(balance)

        if newBal == 0:
            newBal == 1

    with open('balance.txt', 'w') as docWrite:
        docWrite.write(str(newBal))
        print(f"Bet: {bet}\nNew balance: {newBal}\n")
        wait()

def wait():
    if input():
        quit()
    else:
        quit()
    

try:
    os.system('cls')
    print("------------------------- WELCOME TO BLACKJACK -------------------------")
    walletRead
    bet = walletRead()
    
    uCards.append(random.choice(tCards))
    uCards.append(random.choice(tCards))
    dCards.append(random.choice(tCards))
    dCards.insert(1, "~")
    check()

    while True:
        menu(bet)

except ValueError:
        with open('balance.txt', 'w') as docWrite:
            docWrite.write('1')
