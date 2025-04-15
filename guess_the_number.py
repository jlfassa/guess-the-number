import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Guess the Number game!")
    print("I've chosen a number between 1 and 100. Can you guess it?")
    
    while True:
        try:
            # Get the user's guess
            guess = input("\nEnter your guess: ")
            guess = int(guess)
            attempts += 1
            
            # Compare the guess with the secret number
            if guess < secret_number:
                print("Too low, try again")
            elif guess > secret_number:
                print("Too high, try again")
            else:
                print(f"\nCongratulations! You've guessed the number in {attempts} attempts!")
                break
                
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number() 