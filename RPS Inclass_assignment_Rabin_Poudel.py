
import random
 
def get_user_choice():
 """get and validate user choice"""
 while True:
    user_choice = input("enter rock, paper, scissors: ")
    if user_choice in ('rock', 'paper', 'scissors'):
        return user_choice
    else:
        print("invalid response")
        continue


def get_computer_choice():
   """Randomly select a choice from computer and return computer choice"""
   computer_choice = random.choice(['rock','scissors','paper'])
   return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "IT'S A TIE!"
    elif user_choice == 'rock' and computer_choice == 'scissors' or \
        user_choice == 'paper' and computer_choice == 'rock' or \
        user_choice == 'scissors' and computer_choice == 'paper':
        return "YOU WIN!!!!"
    else:
        return "COMPUTER WINS!"
  
def main(): 
   while True:
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()
    print(determine_winner(user_choice, comp_choice))
    play_again = input("play_again: ")
    if play_again.lower() not in ('y','yes'):
       break
   
main()
   
