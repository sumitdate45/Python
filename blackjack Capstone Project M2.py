import random
from tkinter import Y
rt = 90
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def total(n):
    t = 0
    for j in n:
        t += j
    return t

def random_card():
        return random.choice(cards)
def check(m):
    if total(m) > 21:
        if 11 in m:
            m[m.index(11)] = 1
            return 1
        else:
            return 0
    elif total(m) <= 21:
        return 2
play = True
while play:
    want_to_play = input("Do you want to play blackjack type 'y' to play and 'n' to stop: ").lower()
    user_cards = []
    computers_cards = []
    if want_to_play == "y":
        for i in range(2):
            user_cards.append(random.choice(cards))
            computers_cards.append(random.choice(cards))
        print(f"user cards:{user_cards} current score:{total(user_cards)}")
        print(f"computer's First Card: {computers_cards[0]}") 
        should_continue = True
        while should_continue:
            if total(user_cards) == 21 or total(computers_cards) == 21:
                should_continue = False
            else:
                check(user_cards)
                check(computers_cards)
                pick_again = True
                while pick_again:
                    pick = input("Do you want to pick card ? type 'y' to pick 'n' to pass: ").lower()
                    if pick == "y":
                        user_cards.append(random_card())
                        print(f"user cards:{user_cards} current score:{total(user_cards)}")
                        print(f"computer's First Card: {computers_cards[0]}")
                        if check(user_cards) == 1 or check(user_cards) == 2:
                            pick_again = True
                        elif check(user_cards) == 0:
                            pick_again = False
                            should_continue = False
                    elif pick == "n":
                        should_continue = False
                        pick_again = False
        rerun = True
        while rerun:
            if total(computers_cards) < 17:
                computers_cards.append(random_card())
                if total(computers_cards) >= 17:
                    if check(computers_cards) == 1:
                        rerun = True
                    else:
                        rerun = False
                elif total(computers_cards) < 17:
                    rerun = True
            else:
                rerun = False
                
        print(f"Your Final Hand: {user_cards}, Final score: {total(user_cards)}")
        print(f"Computer's Final Hand: {computers_cards}, Final score: {total(computers_cards)}")
        if total(user_cards) == 21:
            print("You Won ! You have a BlackJack")
        elif total(computers_cards) == 21:
            print("You lose ! Computer has a BlackJack")
        elif total(user_cards) >= 22:
            print("You Went Over! You Lose")
        elif total(computers_cards)>= 22:
            print("You Won ! Your opponent went over ")
        elif total(user_cards) > total(computers_cards):
            print("You Win")
        elif total(user_cards) == total(computers_cards):
            print("This was a Draw Nice Try")
        else:
            print("You lose try harder")

    if want_to_play == "n":
        print("Thank You")
        play = False 
            
            
            
    