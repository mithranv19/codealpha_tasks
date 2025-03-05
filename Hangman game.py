import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "software"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if set(word).issubset(guessed_letters):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        if attempts == 0:
            print("\nGame Over! The word was:", word)

if __name__ == "__main__":
    hangman()
