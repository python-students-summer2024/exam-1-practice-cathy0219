"""
Your job is to complete the definitions of each function mentioned in the comments so that it achieves its indicated behavior.

Do not run this file directly.
Rather, call whichever functions defined in this file that you want to run from within the file named main.py and run that file directly.
"""

import random

##--------------------- Function #1 ---------------------##
# Define a function named 'get_random_int'.  
# This function accepts two arguments: a minimum value and a maximum value.
# The function must return a random integer between these two values, inclusive.
# Use the function random.randint() to generate the pseudo-random number.


##--------------------- Function #2 ---------------------##
# Define a function named 'get_guess'.
# This function accepts a single argument - an integer that serves as a max value.
# This function asks the user once to guess a random integer between 1 and the max value, inclusive.
# The function calls the function named get_random_int in order to generate the random integer in this range.
# If the user has entered an invalid response (i.e. anything that is not an integer in this range), the function returns an integer, -1.
# If the user has guessed the random integer correctly, this function returns a boolean True.
# If the user has guessed incorrectly, this function returns a boolean False.


##--------------------- Function #3 ---------------------##
# Define a function named 'play_game'.
# This function does not accept any arguments.
# This function uses the get_guess function to ask the user four times to guess a random integer between 1 and 5, inclusive.
# Each time the user guesses, they are immediately informed whether they guessed correctly or not, with the printed output, "Correct!" or "Wrong!"
# If at any time, the user enters an invalid response, the program immediately prints out the text, "Invalid response!" and does not print out anything further.
# At the end, the function, assuming the user has entered all valid guesses, the program prints out the percent of guesses that user guessed correctly, following the format: "You guessed 75% of the random numbers correctly."

##--------------------- Function #1 ---------------------##
def get_random_int(min_val, max_val):
    """
    This function accepts two arguments: a minimum value and a maximum value.
    The function must return a random integer between these two values, inclusive.
    """
    return random.randint(min_val, max_val)


##--------------------- Function #2 ---------------------##
def get_guess(max_val):
    """
    This function accepts a single argument - an integer that serves as a max value.
    This function asks the user once to guess a random integer between 1 and the max value, inclusive.
    The function calls the function named get_random_int in order to generate the random integer in this range.
    If the user has entered an invalid response (i.e. anything that is not an integer in this range), the function returns an integer, -1.
    If the user has guessed the random integer correctly, this function returns a boolean True.
    If the user has guessed incorrectly, this function returns a boolean False.
    """
    random_int = get_random_int(1, max_val)
    try:
        user_guess = int(input(f"Guess a random integer between 1 and {max_val}: "))
    except ValueError:
        return -1

    if user_guess < 1 or user_guess > max_val:
        return -1

    if user_guess == random_int:
        return True
    else:
        return False


##--------------------- Function #3 ---------------------##
def play_game():
    """
    This function does not accept any arguments.
    This function uses the get_guess function to ask the user four times to guess a random integer between 1 and 5, inclusive.
    Each time the user guesses, they are immediately informed whether they guessed correctly or not, with the printed output, "Correct!" or "Wrong!"
    If at any time, the user enters an invalid response, the program immediately prints out the text, "Invalid response!" and does not print out anything further.
    At the end, the function, assuming the user has entered all valid guesses, the program prints out the percent of guesses that user guessed correctly, following the format: "You guessed 75% of the random numbers correctly."
    """
    max_val = 5
    correct_guesses = 0
    total_guesses = 4

    for i in range(total_guesses):
        result = get_guess(max_val)
        if result == -1:
            print("Invalid response!")
            return
        elif result:
            print("Correct!")
            correct_guesses += 1
        else:
            print("Wrong!")

    percent_correct =int((correct_guesses / total_guesses) * 100)
    print(f"You guessed {percent_correct}% of the random numbers correctly.")