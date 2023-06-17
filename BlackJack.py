import random
from os import system
from time import sleep
from Cards import cards
from Values import values

def BlackJack():
    
    print("Welcome to BalckJack")
    print("Dealing one card each...")
    sleep(1)
    system("cls")
    
    deal = random.choice(cards)
    cards.remove(deal)
    cards_a = [deal]
    a = values(deal,0)
    
    deal = random.choice(cards)
    cards.remove(deal)
    cards_b = [deal]
    b = values(deal,0)
    
    print(f"Your Card: {cards_a}")
    print(f"Dealer's Card: {cards_b}")
    
    deal = random.choice(cards)
    cards.remove(deal)
    cards_a.append(deal)
    a += values(deal,a)
    
    print("Dealing one card each...")
    sleep(2)
    system("cls")
    
    print(f"Your Cards: {cards_a}")
    print(f"Dealer's First Card: {cards_b}")
    
    deal = random.choice(cards)
    cards.remove(deal)
    cards_b.append(deal)
    b += values(deal,b)
    
    while(True):
        call = input("Do you want another card?? Enter 'Y' for Yes and 'N' for No ").upper()
        if(call == 'N'):
            system('cls')
            break
        
        print("Dealing one card each...")
        sleep(1)
        system("cls")
        
        deal = random.choice(cards)
        cards.remove(deal)
        cards_a.append(deal)
        a += values(deal,a)
        
        if(a>21):
            print(f"Your Cards: {cards_a}")
            print(f"Dealer Cards: {cards_b}")
            return False
        
        print(f"Your Cards: {cards_a}")
    
    print(f"Your Cards: {cards_a}")
    print(f"Dealer Cards: {cards_b}")
    
    if(b<17):
        print("Dealing one more card to dealer...")
        sleep(2)
        system("cls")
        
        deal = random.choice(cards)
        cards.remove(deal)
        cards_b.append(deal)
        b += values(deal,b)
        
        print(f"Your Cards: {cards_a}")
        print(f"Dealer's Cards: {cards_b}")
    
    if(b>21):
        return True
    elif(a<b):
        return False
    else:
        return True

system("cls")
if(BlackJack()):
    print("You Win!!")
else:
    print("You Lose!!")
    
 
