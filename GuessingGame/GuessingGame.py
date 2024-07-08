# Kyle Stewart CIS261 LAB: Guessing Game
import random


def guessing_game():
    print("Guess the number")
    limit = input("Enter the limit: ")
    print("I'm thinking of a number from 1 to {limit}")
    random_number = random(1, limit)
    tries = 0
    guess = None
    
    While guess != random_number:
        guess = input("Guess the number: ")
        tries += 1
        if guess < random_number:
            print("Too low.")
        elif guess > random_number:
            print("Too high.")
            
    print("You guessed it in {tries} tries.")
    
def main():
    play_again = "y"
    while play_again.lower() == "y":
        guessing_game()
        play_again = input("Wouuld you like to play again? (y/n): ")
    if play_again.lower() == "n":
        Print("Bye!")

if __name__ = "__main__":
    main()
    