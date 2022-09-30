import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word = word.upper()
    word_letter = set(word) #breaks up word into letters
    alphabet = set(string.ascii_uppercase) #gives a "letter bank" to choose from
    user_letter = set() #tracks user guesses
    right_letters = set()
    guess_number = 20

    print('You have 20 guesses')
    guess = input('guess a letter or a word: ').upper()
    while guess != word:
        if guess in word_letter:
            print(f'{guess} is in the word. You have {guess_number} guesses left')
            right_letters.add(guess)
        if guess not in word_letter:
            guess_number -= 1
            if len(guess) == 1:
                if guess in alphabet:
                    print(f'{guess} is not in the word. You have {guess_number} guesses left')
                if guess not in alphabet:
                    print(f'{guess} is not a valid letter. You have {guess_number} guesses left')
            else:
                print(f'{guess} is not the correct word. You have {guess_number} guesses left')
            if guess_number == 0:
                print(f'you have run out of guesses, game over! The word was {word}')
                quit()
        user_letter.add(guess)
        print('letters/words guessed already: ' + ', '.join(user_letter))
        print('letters in the word: ' + ', '.join(right_letters))
        guess = input('guess a letter or a word: ').upper()

    if guess == word:
        print('You guessed the word')

get_valid_word(words)
hangman()
