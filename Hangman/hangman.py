import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    while len(word_letters) > 0:
        # letters used
        print('You have used these letters : '+', '.join(used_letters))

        # what the current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word : ', ' '.join(word_list))

        user_letter = input('Guess a letter : ').upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You already used this letter.')
        else:
            print('Invalid letter! Try again')


hangman()
