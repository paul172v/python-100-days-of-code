import random

def get_random_word():
    words = ['python', 'developer', 'hangman', 'challenge', 'programming', 'interface']
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"Remaining attempts: {attempts}")
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            print(f"Wrong guess: '{guess}' is not in the word.")
            attempts -= 1
        else:
            print(f"Good job! '{guess}' is in the word.")

        if all(letter in guessed_letters for letter in word):
            print("\n" + display_word(word, guessed_letters))
            print("Congratulations! You've guessed the word correctly!")
            break
    else:
        print(f"\nGame over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
