from cs50 import get_string
import math


def main():

    text = get_string("Text: ")    # gets input from user
    letters = 0
    words = 0
    sentences = 0

    for c in text:
        if c.isalpha() is True:  # counts letters
            letters += 1
        if c == '.' or c == '?' or c == '!':    # counts punctuation/sentences
            sentences += 1
        if c == ' ':
            words += 1
    words += 1    # adds 1 to number of spaces to get the number of words.

    # Calculates the Coleman-Liau Index
    l = letters / words * 100
    s = sentences / words * 100
    index = round(0.0588 * l - 0.296 * s - 15.8)

    # Prints the grade level from the Coleman-Liau Index
    if index < 1:
        print("Before Grade 1")
    if index >= 16:
        print("Grade 16+")
    if index > 1 and index < 16:
        print(f"Grade {index}")


main()