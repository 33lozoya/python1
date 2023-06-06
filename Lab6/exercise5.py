# Write a program that asks the user to enter a String. Calculate and count the number of spaces in the String entered. Print the number of spaces.
# Based on the number of spaces print the word count for that sentence (you can assume that the sentence is entered correctly follows usual format for an English sentence).

sentence = input("Please enter a sentence: ")

# deleted line

for character in sentence:
    if character == " ":
        spaceCount += 1
# deleted line
