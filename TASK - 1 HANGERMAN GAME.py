import random

# Step 1: Predefined list of words
words = ["apple", "banana", "grape", "orange", "mango"]

# Step 2: Choose a random word
word = random.choice(words)
word_letters = list(word)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("_ " * len(word))  # Display blanks for the word

# Step 3: Main game loop
while wrong_guesses < max_wrong:
    guess = input("Guess a letter: ").lower()

    # Validate single letter input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word_letters:
        print("Good guess!")
    else:
        wrong_guesses += 1
        print(f"Wrong guess! You have {max_wrong - wrong_guesses} tries left.")

    # Display current progress
    display_word = ""
    for letter in word_letters:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)

    # Check for win
    if all(letter in guessed_letters for letter in word_letters):
        print("🎉 Congratulations! You guessed the word!")
        break
else:
    print(f"😢 Game Over! The word was '{word}'.")
