number = 10
attempts = 5

print("I'm thinking of a number...")

while attempts > 0:
    guess = input(f"What number am I thinking of? (You have {attempts} attempts left) (Enter 'q' to quit) ")
    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break
    try:
        guess = int(guess)
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        attempts -= 1
        if attempts == 0:
            print(f"Game over! The number was {number}.")
    except ValueError:
        print("Please enter a valid number.")
