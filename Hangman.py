import random

words = ["python", "computer", "program", "hangman", "coding"]
word = random.choice(words)

guessed = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")

while wrong_guesses < max_guesses:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if all(letter in guessed for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed this letter.")
        continue

    guessed.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining guesses:", max_guesses - wrong_guesses)
    else:
        print("Correct guess!")

if wrong_guesses == max_guesses:
    print("\nGame Over!")
    print("The word was:", word)
