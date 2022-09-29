import random

allowed_errors = 7
done = False
word_list = ["brick", "click", "freak", "chick"]
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess_number = input("Guess how many letters in this word? ")
guess = input("Guess a letter: ").lower()
word = ""
# TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
if int(guess_number) == len(chosen_word):
    print(len(chosen_word))
else:
    print("inc")
while not done:
    for letter in chosen_word:
        if letter in guess:
            letter.replace("_", guess)
            print(letter, end=" ")
        else:
            print("_", end=" ")

    Another_guess = input(f"Allowed Errors Left {allowed_errors}, Next Guess: ")
    word += guess
    if Another_guess not in chosen_word:
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True
    for letter in chosen_word:
        if letter.lower() not in guess:
            done = False
if done:
    print(f"You found the word! It was {word}!")
else:
    print(f"Game Over!")
HANGMAN_PICS = ['''
  3.   +---+
  4.       |
  5.       |
  6.       |
  7.      ===''', '''
  8.   +---+
  9.   O   |
 10.       |
 11.       |
 12.      ===''', '''
 13.   +---+
 14.   O   |
 15.   |   |
 16.       |
 17.      ===''', '''
 18.   +---+
 19.   O   |
 20.  /|   |
 21.       |
 22.      ===''', '''
 23.   +---+
 24.   O   |
 25.  /|\  |
 26.       |
 27.      ===''', '''
 28.   +---+
 29.   O   |
 30.  /|\  |
 31.  /    |
 32.      ===''', '''
 33.   +---+
 34.   O   |
 35.  /|\  |
 36.  / \  |
 37.      ===''']
