# number_guessing_game.py
import random

def play_number_guessing_game():
    secret = random.randint(1, 100)   # pick a number between 1 and 100
    attempts = 0

    print("=" * 55)
    print("🎯  WELCOME TO THE NUMBER GUESSING GAME  🎯")
    print("=" * 55)
    print("I'm thinking of a number between 1 and 100.")
    print("Type your guess and press Enter.")
    print("Type 'q' or 'quit' to exit anytime.\n")

    while True:
        user_input = input("Enter your guess (1-100) or 'q' to quit: ").strip()

        # allow quitting
        if user_input.lower() in ("q", "quit"):
            print("You quit the game. Bye!")
            break

        # validate integer input
        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a valid integer between 1 and 100 (or 'q' to quit).")
            continue

        # validate range
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100. Try again.")
            continue

        attempts += 1

        # give feedback
        if guess < secret:
            print("Too LOW. Try again.\n")
        elif guess > secret:
            print("Too HIGH. Try again.\n")
        else:
            print(f"🎉 Correct! The number was {secret}.")
            print(f"You found it in {attempts} attempt{'s' if attempts != 1 else ''}.\n")
            # ask if they want to play again
            play_again = input("Play again? (y/n): ").strip().lower()
            if play_again in ("y", "yes"):
                secret = random.randint(1, 100)
                attempts = 0
                print("\nI've chosen a new number between 1 and 100. Good luck!\n")
                continue
            else:
                print("Thanks for playing — goodbye!")
                break

if __name__ == "__main__":
    play_number_guessing_game()
