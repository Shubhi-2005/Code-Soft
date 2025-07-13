#Rock-Papers-Scissors Game
import random

user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors Game!")
print("Instructions: Type 'rock', 'paper', or 'scissors' to play.")

while True:
    # User Input
    user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()

    # Validate user input
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        continue

    # Computer Selection
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    # Display Choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game Logic
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    # Display Result
    print(result)

    # Score Tracking
    print(f"Score => You: {user_score} | Computer: {computer_score}")

    # Play Again
    play_again = input("\n Do you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print("\n Thanks for playing!")
        print(f" Final Score => You: {user_score} | Computer: {computer_score}")
        break