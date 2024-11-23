import random

def get_computer_choice():
    return random.choice(["stone", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "stone" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or  (user_choice == "paper" and computer_choice == "stone"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Stone-Paper-Scissors! game")
    while True:
        print("\nEnter your choice: stone, paper, or scissors (or 'exit' to quit the game)")
        user_choice = input("Your choice: ").strip().lower()
        
        if user_choice == "exit":
            print("Thanks for playing!")
            break
        
        if user_choice not in ["stone", "paper", "scissors"]:
            print("Invalid choice Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
