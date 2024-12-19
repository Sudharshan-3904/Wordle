import requests
import random
import os

def fetch_random_word():
    """
    Fetch a random word from an API.
    Returns:
        str: A random word (in lowercase).
    """
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        response.raise_for_status()
        word = response.json()[0]
        return word.lower()
    except requests.RequestException as e:
        print(f"Error fetching the word: {e}")
        return None

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def get_guess():
    """Prompt the player to enter a guess."""
    while True:
        guess = input("Enter your 5-letter guess: ").lower().strip()
        if len(guess) == 5 and guess.isalpha():
            return guess
        print("Invalid guess. Please enter exactly 5 letters.")

def display_feedback(guess, target_word):
    """
    Display feedback for a guess.
    Green: Letter is correct and in the correct position.
    Yellow: Letter is correct but in the wrong position.
    Gray: Letter is not in the word.

    Args:
        guess (str): The player's guess.
        target_word (str): The target word.
    """
    feedback = []
    for g_char, t_char in zip(guess, target_word):
        if g_char == t_char:
            feedback.append(f"\033[92m{g_char}\033[0m")  # Green for correct position
        elif g_char in target_word:
            feedback.append(f"\033[93m{g_char}\033[0m")  # Yellow for correct letter, wrong position
        else:
            feedback.append(f"\033[90m{g_char}\033[0m")  # Gray for incorrect letter
    print(" ".join(feedback))

def wordle_game():
    """Run the Wordle game."""
    target_word = fetch_random_word()
    if not target_word:
        print("Unable to start the game due to an error fetching the word.")
        return

    clear_screen()
    print("Welcome to Wordle! You have 6 attempts to guess the 5-letter word.")

    attempts = 6
    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        guess = get_guess()

        if guess == target_word:
            print(f"\033[92mCongratulations! You've guessed the word: {target_word}\033[0m")
            break

        display_feedback(guess, target_word)
        attempts -= 1

    if attempts == 0:
        print(f"\nGame Over! The word was: {target_word}")

if __name__ == "__main__":
    wordle_game()