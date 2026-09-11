import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects random word."""
    word = random.choice(WORDS)
    return word


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays snowman and the current word."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print()


def play_game():
    """Runs Snowman Meltdown game."""

    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()
        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1
        word_guessed = True

        for letter in secret_word:
            if letter not in guessed_letters:
                word_guessed = False

        if word_guessed:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You saved the snowman!")
            return

    display_game_state(mistakes, secret_word, guessed_letters)

    print(f"The snowman melted! The word was: {secret_word}")


if __name__ == "__main__":
    play_game()
