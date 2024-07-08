# Kyle Stewart CIS261 LAB: Guessing Game
import random


def guessing_game():
    print("Guess the number!")
    limit = int(input("Enter the limit: "))
    print(f"I'm thinking of a number from 1 to {limit}")
    random_number = random.randint(1, limit)
    guess = None
    tries = 0
    
    while guess != random_number:
        guess = int(input("Guess the number: "))
        tries += 1
        if guess < random_number:
            print("Too low.")
        elif guess > random_number:
            print("Too high.")
            
    print(f"You guessed it in {tries} tries.")
    
def main():
    play_again = "y"
    while play_again.lower() == "y":
        guessing_game()
        play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() == "n":
        print("Bye!")

if __name__ == "__main__":
    main()
    