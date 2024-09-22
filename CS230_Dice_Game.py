import random

'''
1. Initialize two dice with 6 sides each, which can be customized later if desired.
2. Set the variable `active` to `True` to control the main game loop.

3. Start the main game loop using a `while` loop with the condition `active`.

4. Within the loop:
   - Simulate a roll of two dice (one for the computer and one for the player) with the number of sides specified earlier.
   - Display the results of both rolls, indicating the computer's roll and the player's roll.

5. Compare the computer's roll and the player's roll to determine the outcome:
   - If the computer's roll is greater than the player's roll, print "Computer Wins!"
   - If the computer's roll is less than the player's roll, print "Player Wins!"
   - If both rolls are equal, print "It's a draw!"

Hint! Prompt the player to decide whether they want to roll the dice again.
   
   - Start a nested `while` loop for input validation, which continues until a valid choice is made.
   - Within this loop, ask the player, "Roll again? (yes/no): "
   - Accept the player's input and convert it to lowercase.
   - Check if the input is one of the following: 'yes', 'no', 'y', or 'n'.
   - If the input is valid, exit the input validation loop; otherwise, inform the player that the input is invalid and ask them to enter 'yes' or 'no'.

Hint! After exiting the input validation loop, check the player's choice:
   - If the player chooses 'no' or 'n', print "Thanks for Playing!" and set `active` to `False` to exit the main game loop.
   - If the player chooses 'yes' or 'y', the game continues, and another round of dice rolling begins.''' 


   #My code begins from here: 

active = True            

while active:                          #starting the main loop
    dice_size = 6                        #initializing the dice with 6 sides which can be customized later as well
    dice1= random.randint(1,dice_size)   #simulating the roll of both dices
    dice2 = random.randint(1,dice_size )
    print("The values are :")               #displaying the results
    print(f"\n Computer's roll={dice1}")
    print(f" Player's roll={dice2}")
    if dice1>dice2:                     #determing the outcomes
        print("Compter wins!")
    elif dice1<dice2:
        print("Player wins!")
    else:
        print("It's a draw!")

    while True:                 #nested while loop for player input validation        
      player_choice = input("You want to roll again??(yes/no):  ").lower()   #prompt the player if he wants to play again or not
      if player_choice in ['yes','no','y','n']:
          break
      else:
       print("Invalid Input. Please type yes or No!")

    #input validation and act according their choice to play again or not
    if player_choice in ['no', 'n']:       
        print("Thanks for Playing!")
        active = False
    elif player_choice in ['yes', 'y']:
     print("Welcome Again !")
     continue 
