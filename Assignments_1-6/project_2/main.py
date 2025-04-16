import random

def computer_guess():
    print("Think of a number between 1 and 100, and I will try to guess it!")
    low = 1
    high = 100
    feedback = ''
    attempts = 0

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Only one possible number left

        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it too high (h), too low (l), or correct (c)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Please enter 'h', 'l', or 'c'.")

    print(f"I guessed it! The number is {guess}. It took me {attempts} attempts.")

# Start the game
computer_guess()
