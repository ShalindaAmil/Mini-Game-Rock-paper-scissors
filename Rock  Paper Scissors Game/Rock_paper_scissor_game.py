import random

#get chices from user
def get_choices():
    player_choice=input("Enter a choice (rock, paper,scieeors): ")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

#check who is win?
def check_win(player,computer):
    print(f"you chose {player}, computer chose {computer}")
    if player==computer:
        return "It is a tie!" 
    elif player=="rock":
        if computer=="scissors":
            return "Rock smashes scissors! you win :)"
        else:
            return "Paper covers rock! you lose :("
    elif player=="paper":
        if computer=="rock":
            return "Paper covers rock! you win :)"
        else:
            return "Scissors cut paper! you lose :("
    elif player=="scissors":
        if computer=="paper":
            return "Scissors cut paper! you win :)"
        else:
            return "Rock smashes scissors! you lose :( "
        
choices =  get_choices()
result=check_win(choices["player"],choices["computer"])
print (result)
