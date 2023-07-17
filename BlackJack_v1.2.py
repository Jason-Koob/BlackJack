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
        print(f"H -> Hit\nD -> Double-down\nS -> Stay\n")
        play = input()

        if play == 'H' or play == 'h':
            uCards.append(random.choice(tCards))

        elif play == 'D' or play == 'd':
            bet = int(bet) + int(bet)
            time.sleep(.5)
            print(f"Your bet is now {bet}.\n")
            uCards.append(random.choice(tCards))

        elif play == 'S' or play == 's':
            dCards.append(random.choice(tCards))
        else:
            count()

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
    print(f"Your cards are worth {uValue}.\n")

def dEval():

    global dValue

    dValue = 0

    for i in dCards:
        if i == 'J':
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
    print(f"The dealer has cards worth {dValue}.\n")

def uCheck():

    if int(uValue) == 21:
        print(f"YOU GOT A BLACKJACK!\n")
        walletWin(bet)
        
    elif int(uValue) > 21:
        print(f"YOU BUSTED!\n")
        walletLoss(bet)
        pass

    elif int(uValue) < 21:
        pass

    elif int(uValue) == 21 and int(dValue) == 21:
        print(f"PUSH!\n")
    

def dCheck():

    if int(dValue) == 21:
        print(f"THE DEALER GOT A BLACKJACK!\n")
        walletLoss(bet)
        pass

    elif int(dValue) > 21:
        print(f"THE DEALER BUSTED!\n")
        walletWin(bet)
        pass

    elif int(dValue) < 21:
        pass

    elif int(uValue) == 21 and int(dValue) == 21:
        print(f"PUSH!\n")
        pass

    if int(dValue) > 17:
        dCards.append(random.choice(tCards))
        count()

def count():

        uEval()
        time.sleep(.5)

        dEval()
        time.sleep(.5)

        uCheck()
        dCheck()

def walletRead():

    global allowBet
    global run

    while allowBet == True:
        with open('balance.txt', 'r') as docRead:
            docRead = docRead.read()

            if docRead == "0":
                docRead = int(docRead) + 1
            
            print(f"Your balance is: {int(docRead)}.\nHow many would you like to bet?:\n")
            bet = input()
              
            if int(docRead) >= int(bet) and int(bet) >= 0:
                allowBet = True
                return bet
            else:
                allowBet == False
                os.system('cls')
                print(f"You cannot bet {int(bet)} as you only have {docRead}.\n")
        
def walletWin(bet):

    global run

    with open('balance.txt', 'r') as file:
        balance = file.read()
        file.read = balance
        newBal = int(bet) + int(balance)

        if newBal == 0:
            newBal == 1

    with open('balance.txt', 'w') as docWrite:
        docWrite.write(str(newBal))
        print(f"Bet: {bet}\nNew balance: {newBal}")
        time.sleep(3)
        quit()
        
def walletLoss(bet):

    global run
    
    with open('balance.txt', 'r') as file:
        balance = file.read()
        file.read = balance
        newBal = -int(bet) + int(balance)

        if newBal == 0:
            newBal == 1

    with open('balance.txt', 'w') as docWrite:
        docWrite.write(str(newBal))
        print(f"Bet: {bet}\nNew balance: {newBal}")
        time.sleep(3)
        quit()

try:
    walletRead
    run = True
    os.system('cls')
    print("------------------------- WELCOME TO BLACKJACK -------------------------")

    

    uCards.append(random.choice(tCards))
    uCards.append(random.choice(tCards))
    dCards.append(random.choice(tCards))
    bet = walletRead()

    while run == True:
        count()
        menu(bet)

except ValueError:
        with open('balance.txt', 'w') as docWrite:
            docWrite.write('1')