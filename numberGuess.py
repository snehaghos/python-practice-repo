# Number Guessing Game
# Computer picks a number, you guess it!
# Easy logic: just compare and give hints

import random

def number_guessing_game():
    print("=== NUMBER GUESSING GAME ===")
    print("I'm thinking of a number between 1 and 50.")
    print("Try to guess it!")
    print("-" * 35)

    secret = random.randint(1, 50)
    attempts = 0
    max_attempts = 7
    guessed_numbers = []

    while attempts < max_attempts:
        # Get player guess
        while True:
            try:
                guess = int(input(f"\nAttempts left: {max_attempts - attempts} | Your guess (1-50): "))
                if guess < 1 or guess > 50:
                    print("Please enter a number between 1 and 50!")
                    continue
                if guess in guessed_numbers:
                    print("You already guessed that! Try a different number.")
                    continue
                break
            except ValueError:
                print("Enter a valid number!")

        attempts += 1
        guessed_numbers.append(guess)

        # Check the guess
        if guess == secret:
            print(f"\n*** CORRECT! You got it in {attempts} attempt(s)! ***")
            print(f"The secret number was: {secret}")

            if attempts == 1:
                print("Incredible! First try!")
            elif attempts <= 3:
                print("Amazing! You're a genius!")
            elif attempts <= 5:
                print("Great job! Well done!")
            else:
                print("You got it! Nice work!")
            return

        elif guess < secret:
            print("Too LOW! Go higher.")
        else:
            print("Too HIGH! Go lower.")

        # Extra hint after 4 attempts
        if attempts == 4:
            if abs(guess - secret) <= 5:
                print("  (You're very close!)")
            elif abs(guess - secret) <= 10:
                print("  (Getting warmer...)")
            else:
                print("  (You're still far off!)")

    # Out of attempts
    print(f"\nGame Over! You used all {max_attempts} attempts.")
    print(f"The secret number was: {secret}")
    print("Better luck next time!")

if __name__ == "__main__":
    number_guessing_game()
    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() == "y":
        number_guessing_game()
