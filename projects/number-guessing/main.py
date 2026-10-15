import random

secret_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Chosen difficulty: easy, medium, hard")
difficulty = input("Choose difficulty (easy/medium/hard): ").strip().lower()

def check_guess(guess, secret_number):
    if guess > secret_number:
        return "Too high"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Correct"
    
while difficulty not in ["easy", "medium", "hard"]:
    print("Invalid difficulty level. Please choose 'easy', 'medium', or 'hard'.")
    difficulty = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ").lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "medium":
    attempts = 7
else:
    attempts = 5

print(f"You have {attempts} attempts to guess the number.")



while attempts > 0:
    print(f"You have {attempts} attempts left.")

    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guess < 1 or guess > 100:
        print("Please choose a number between 1 and 100.")
        continue

    result = check_guess(guess, secret_number)
    print(result)

    if result == "Correct":
        print("Congratulations! You won!")
        break

    attempts -= 1

else:
    print(f"Game Over! The number was {secret_number}")