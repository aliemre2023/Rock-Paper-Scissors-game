import random

print("YOO!..\nKid come here. \nWho are you? What do you do in there. \nTsch! \nYou suppose that I'll belive to tis lie!!!! You stupit boy. \nOK! \nI'll give you a chace to get rid of me. \nIf you win this game, you will go to your home. \nLet's starts!!")

selections = ["rock","paper","scissors"]

round_time = input("How many round do you want to play? : ")

round_counter = 0

comp_score = 0
plyr_score = 0

while int(round_time) != round_counter:
    round_counter += 1

    computer_choice = random.choice(selections)
    player_choice = input("--rock, paper or scissors-- \nChoice one of them: ")

    if player_choice == "rock":
        if computer_choice == "rock":
            print("*Equal","\n--------")
        elif computer_choice == "paper":
            print("*My selection was paper. I won this round!","\n--------")
            comp_score +=1
        elif computer_choice == "scissors":
            print("*You won this round!","\n--------")
            plyr_score += 1

    elif player_choice == "paper":
        if computer_choice == "rock":
            print("*You won this round!","\n--------")
            plyr_score += 1
        elif computer_choice == "paper":
            print("*Equal","\n--------")
        elif computer_choice == "scissors":
            print("*My selection was paper. I won this round!","\n--------")
            comp_score += 1

    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("*My selection was scissors. I won this round!","\n--------")
            comp_score += 1
        elif computer_choice == "paper":
            print("*You won this round!","\n--------")
            plyr_score +=1
        elif computer_choice == "scissors":
            print("*Equal","\n--------")

    else:
        print("Please enter a valid value...","\n--------")
        round_counter -= 1
        

if plyr_score == comp_score:
    print("-"*30,"\nDa hell boi we have same score. \nLook what I say. \nMy mother cooked a beef. \nI'd rather to eat beef than eat you. \nSee you bro :)")
elif plyr_score >= comp_score:
    print("-"*30,"\nWoa. \nYou're good at this game. See you bro.")
elif plyr_score <= comp_score:
    print("-"*30,"\n:).")