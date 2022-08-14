import random
from words import words
import re

print("Welcome to hangman. Guess the word by spelling it out entirely.")

def game():
    death_count = [1, 1, 1, 1, 1, 1]
    need_word = random.choice(words)
    word_length = len(need_word)
    letter_guess = ""
    word_guess = ""
    is_present = ""
    word_list = []
    used_letters = []
    for i in range(len(need_word)):
        word_list.append("_")
    while not(''.join(word_list) == need_word or len(death_count)==0):
        print("Here are your used letters: ", end = "")
        print(*used_letters)
        print(*word_list)
        letter_guess = input("What letter would you like to guess?")
        if isinstance(letter_guess, str) != True: #how to get other data types not included?
            print("That's not a valid input")
        elif need_word.find(letter_guess)==-1:
            print("That letter is not in the word!")
            death_count.remove(1)
            used_letters.append(letter_guess)
            print(f"You have {len(death_count)} tries left\n")
        else:
            print("It's in the word!")
            indexes = [x.start() for x in re.finditer(letter_guess, need_word)]
            # WE LOVE STACK OVERFLOW
            for times in range(len(indexes)):
                word_list[indexes[times]]=letter_guess
            print(f"You have {len(death_count)} tries left \n")
    if len(death_count)==0:
        print(f"You have lost. The word was {need_word}")
    else:
        print(f"You won! The word was {need_word}")
game()
