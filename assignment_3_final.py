# your split into separate methods is not optimal.  Mainly there is too much reliance on global variables.
# better would have been to hide these in some main function, say prs_game() and pass them to all the supporting 
# functions on per need to know basis


import random

running1 = True #Runs while the game is valid. False when user bets out of range.
first_round = True #Use for first round - don't allow user to bet out of range.
user_pick = 0 
game_rounds = 0 
u_total_wins = 0
u_total_points = 0
#might want to keep track of ties, as well

def who_wins(user_pick):
    computer_pick = random.randint(1, 3)
  
    #prints computer choice
    if computer_pick == 1:	# variable computer_pick should be passed to this function as a variable
        print("Computer picked ROCK")
    elif computer_pick == 2:
        print("Computer picked PAPER")
    else:
        print("Computer picked SCISSORS")

	# the following (gray highlight) could have been further relegatd to another function
	# all those magenta numbers are “magic” you should define them 
    #determines winner    
    if (user_pick == computer_pick):
        final_winner = 1
    elif (user_pick == 2 and computer_pick == 3):
        print("Computer WINS!")
        final_winner = 2
    elif (user_pick == 3 and computer_pick == 1):
        print("Computer WINS!")
        final_winner = 2
    elif (user_pick == 3 and computer_pick == 2):
        print("You WIN!")
        final_winner = 1
    else:
        print("Uh oh something's buggy!")
#Final winner is returned as a number. 0=TIE 1=USER 2=COMPUTER
    return final_winner

def validate_input(inp):
    validation = True
    while validation:
        try:
            inp = int(input("I choose: "))
            validation = False
        except ValueError:
            print("Seriously? That's not a number!")
            continue
    return inp


# this should be hidden away in a “amin” function, say prs_game() (as suggested above.
# all global variables should be local to that function
#Main Loop Begins Here

print("Welcome to ROCK PAPER SCISSORS!")
print("Rock breaks scissors, scissors cuts paper, paper covers rock.")
print("------------------------------------------------------------")

while running1:
    bet_value = 0
    running2 = True
    
    print("------------------------------------------------------------")
    print("Bet a number from 1-10 to play, any other number to exit")

    bet_value = validate_input(bet_value)


    while first_round:
        if bet_value < 1 or bet_value > 10:
            print("You need to play at least once! Enter a number within range.")
            bet_value = validate_input(bet_value)
            continue
        else:
            first_round = False
        
    if bet_value < 1 or bet_value > 10:     
        print("You exited game...bye!")
        print("WE PLAYED ", game_rounds, " ROUND(S)")
        print("YOU WON: ", u_total_wins, " TIME(S)")
        print("YOU GAINED: ", u_total_points, " POINT(S)")
        print("Thanks for playing!")
        running1 = False
    else:
        game_rounds+=1
        
        while running2:
            print("Enter 1 for ROCK | 2 for PAPER | 3 for SCISSORS ")
            user_pick = validate_input(user_pick)
            
            if user_pick > 0 and user_pick < 4:
                win = who_wins(user_pick)
                
                #Calculates points and wins for user
                if win == 1:
                    u_total_wins +=1
                    u_total_points +=bet_value
                elif win == 2:
                    u_total_points -=bet_value
                else:
                    u_total_wins = u_total_wins
                    u_total_points = u_total_points
                running2 = False
            else:
                print("Out of range :(")
#running2 and first_round mechanism is awkward.              
