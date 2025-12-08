import random

def start_game():
    """Runs the Number Guessing Game based on the user's initial logic."""
    print("""
Welcome to the Number Guessing Game!
Pick a difficulty level:
1. Easy (10 attempts)
2. Medium (7 attempts)
3. Hard (5 attempts) 
""") # Adjusted the numbering in the display text for clarity

    difficulty = input("Choose a difficulty. Type 'easy','medium' or 'hard': ").lower()
    difficulty = difficulty.strip() 
    
    # Determine the number of attempts
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'medium' :
        attempts = 7
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Invalid choice. Defaulting to 'easy' difficulty.")
        attempts = 10

    # Generate the secret number
    secret_number = random.randint(1, 100)
    print("\nI'm thinking of a number between 1 and 100.")

    # Main game loop
    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        
        # Input handling (Kept original logic, but be aware of potential ValueError if input is not an integer)
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if guess < secret_number:
            print(f"{guess} is too low. Try something higher.")
        elif guess > secret_number:
            print(f"{guess} is too high. Try something lower.")
        else:
            print(f"\n🎉 You got it! The answer was **{secret_number}**.")
            return # Use return to exit the function when the game is won

        attempts -= 1

        if attempts == 0:
            print(f"\n💔 You've run out of guesses. The number was **{secret_number}**. Game over.")

# To run the game, you now just call the function:
while  True:
    start_game()
    play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye.")
        break   