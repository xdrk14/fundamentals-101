#word frequency counter
text = input("Enter a string to count word frequency: ")
word = input("Enter a word to count its frequency: ")
print(text.count(word))

#palinedrome checker
input_string = str(input("Enter a string to check if it's a palindrome: "))
input_string = input_string.upper().strip()
palindrome = input_string[::-1]

if input_string == palindrome:
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")

#guessing game
from itertools import count
import random

random_number = random.randint(1,10)
while random_number != 0:
    user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess == random_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Sorry, that's not the correct number. Try again!")


