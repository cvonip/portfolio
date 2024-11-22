import random  # This lets us generate random numbers

# Step 1: Generate a random number
number_to_guess = random.randint(1, 100)  # Random number between 1 and 100

# Step 2: Explain the game
print("Welcome to the Guess-the-Number Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?")

# Step 3: Start the guessing loop
while True:
    # Ask the user for their guess
    guess = input("Enter your guess: ")

    # Make sure it's a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    # Convert the input to an integer
    guess = int(guess)

    # Step 4: Check if the guess is correct
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it!")
        break  # End the loop when the guess is correct
