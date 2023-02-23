import random

# Define the list of characters to choose from
all_chars = [chr(i) for i in range(256)]

# Define a list of fun messages for when the player guesses correctly
fun_messages = [
    "You're a genius!",
    "Awesome! You got it!",
    "You're on fire! Keep going!",
    "Great job! You're killing it!",
    "That was easy for you, right?",
]

# Define a list of encouraging messages for when the player guesses incorrectly
encouraging_messages = [
    "Don't worry, you'll get it next time!",
    "Almost there! Keep trying!",
    "You're so close, don't give up!",
    "You're doing great, just one more try!",
    "Don't give up, you're getting better!",
]

# Initialize the player's score and number of guesses
score = 0
guesses = 0

# Set up a loop to play the game ten times
for i in range(10):

    # Pick a random character from the list
    char = random.choice(all_chars)

    # Prompt the user to guess the ASCII value
    guess = input(f"What is the ASCII value of '{char}'? ")

    # Convert the guess to an integer
    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Check if the guess is correct
    if guess == ord(char):
        score += 1
        print(random.choice(fun_messages))
    else:
        print(f"Sorry, the correct answer was {ord(char)}. {random.choice(encouraging_messages)}")

    # Increase the number of guesses
    guesses += 1

# Print the player's final score
print(f"Thanks for playing! Your final score is {score} out of {guesses} guesses.")
