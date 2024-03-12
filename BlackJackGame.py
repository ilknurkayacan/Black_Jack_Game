# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:47:18 2024

@author: ilknu
"""
"""
import re

url=input("What is your url?: ")
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url,re.IGNORECASE):
    print(f"Usernaeme: ",matches.group(1))
"""

import random




def deal_card():
   card=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   return random.choice(card)
    

    
print("Welcome to BlackJack\nExit----> X\nContinue----> Y")

while True:
    player=[]
    computer=[]
    player_total=0
    computer_total=0
    
    for i in range(0,2):
        player.append(deal_card())
        player_total += int(player[i])
    
    print("Player Cards: ", player)
    print("Player Cards sum: ", player_total)
    
    for i in range(0,2):
        computer.append(deal_card())
        computer_total +=int(computer[i])
    
    print("Computer cards: ",computer)
    print("Computer Cards sum: ", computer_total)
    
    if player_total>21:
        print("Winner: Computer, ",computer_total)
        choice=input("Your select Exit or Continue ?").strip().lower()
        if choice =="y":
            continue
        elif choice =="x":
            break
    elif computer_total>21:
        print("Winner: Player, ",player_total)
        choice=input("Your select Exit or Continue ?").strip().lower()
        if choice =="y":
            continue
        elif choice =="x":
            break
    
    while True:    
        ask=input("Do you want a card?  Y or N").strip().lower()
        if ask=="y":
            player.append(deal_card())
            if int(player[len(player)-1]) == 11:
                if player_total< 21 and (player_total + int(player[len(player)-1]))<21:
                    player_total +=player[len(player)-1]
                elif player_total< 21 and (player_total + int(player[len(player)-1]))>21:
                    player_total +=1
            else:
                player_total += int(player[len(player)-1])
                    
            print("Player Cards: ", player)
            print("Player Cards sum: ", player_total)
            if player_total>21:
                print("Winner: Computer, ",computer_total)
                choice=input("Your select Exit or Continue ?").strip().lower()
                if choice =="y":
                    continue
                elif choice =="x":
                    break
            if player_total>computer_total:
                computer.append(deal_card())
                computer_total += int(computer[len(computer)-1])
                if computer_total>21:
                    print("Computer: ", computer)
                    print("Computer Sum: ",computer_total)
                    print("Winner: Player, ",player_total)
                    break
        elif ask=="n":
            if player_total>21:
                print("Winner: Computer, ",computer_total)
            elif player_total<=21 and player_total>computer_total:
                print("Winner: Player, ",player_total)
            elif computer_total<=21 and computer_total>player_total:
                print("Winner: Computer, ",computer_total)
            elif computer_total>21:
                print("Winner: Player, ",player_total)
            elif computer_total == player_total:
                print(f"Equal\nComputer: {computer_total}\nPlayer: {player_total}" )
            break
    choice=input("Your select Exit or Continue ?").strip().lower()
    if choice =="y":
        continue
    elif choice =="x":
        break