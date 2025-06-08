import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on game rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def rock_paper_scissors():
    """Main function to run the game."""
    user_score, computer_score = 0, 0

    while True:
        print("\nRock, Paper, Scissors Game!")
        user_choice = input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
        
        if user_choice == "exit":
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            print("Thanks for playing!")
            break
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "You win!" in result:
            user_score += 1
        elif "Computer wins!" in result:
            computer_score += 1
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")

rock_paper_scissors()
