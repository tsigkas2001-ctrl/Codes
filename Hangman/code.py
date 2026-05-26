import random

guessed_letters = []
words_list = []
lives = 6

with open("word.txt", "r") as f:
    words_list = f.readlines()
    secret_word = random.choice(words_list).strip()


while lives > 0:
    
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()

    guess = input("Give me a letter: ").lower()    
    
    if guess in secret_word:
        print("Correct!")
        guessed_letters.append(guess)

    else:
        print("Wrong!")
        lives -=1 