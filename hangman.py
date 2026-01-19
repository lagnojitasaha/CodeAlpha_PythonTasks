#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

# List of words
words = ["apple", "banana", "grapes", "orange", "mango"]

# Randomly choose a word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", display_word)

    if display_word == word:
        print("🎉 Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        attempts -= 1
        guessed_letters.append(guess)
        print("Wrong guess! Attempts left:", attempts)

if attempts == 0:
    print("❌ Game Over! The word was:", word)


# In[ ]:




