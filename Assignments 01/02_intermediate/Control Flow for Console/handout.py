import random

# Constants
NUM_ROUNDS = 5  # Set the number of rounds

def high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score = 0

    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_number}")
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {user_number}")
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()

        # Input validation
        while guess not in ["higher", "lower"]:
            guess = input("Please enter either 'higher' or 'lower': ").strip().lower()

        # Determine result
        if user_number > computer_number and guess == "higher":
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif user_number < computer_number and guess == "lower":
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        # Display score
        print(f"Your score is now {score}\n")

    # Conditional ending messages
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Run the game
if __name__ == "__main__":
    high_low_game()
