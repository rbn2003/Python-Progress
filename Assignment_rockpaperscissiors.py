import random 

def get_user_choice():
    """prompts the user for their choice and validates the input"""
    return input("Choose Rock, Paper, Scissors: ").lower()
        

def get_computer_choice():
    """Randomly selects a choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """compares the user's choice with the computer's choice to determine the winner"""
    
    if user_choice == computer_choice:
        return "TIE"

    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):

        return "YOU WIN"
    else:
        return "COMPUTER WIN"
    

def main():
    print("Welcome to Rock, Paper and Scissors Game!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You choose: {user_choice}")
        print(f"Computer choose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("You want to play again? (Y/N): ")
        if play_again != "N":
            break
        print("Thanks for playing !") 

main()

    
    
    
