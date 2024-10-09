import random

randomNum = random.randint(1, 9)
count = 0

print("Guess the number between 1 and 9. You have 3 chances!")

while True:
    try:
        userInput = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    count += 1
    
    if randomNum == userInput:
        print("Your guess is correct!")
        print(f"You guessed it in {count} attempt(s).")
        break
    
    if count >= 3:
        print(f"Sorry, you've used all 3 guesses. The correct number was {randomNum}.")
        print("You lost the game.")
        break
    
    print("Try again!")
