# Your task here is very special: you must design a vowel eater! Write a program that uses:

# a for loop;
# the concept of conditional execution (if-elif-else)
# the continue statement.

user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)