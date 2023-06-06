# Write a program that takes in two items. A sentence from a user and a single character.
# You must include validation that if the user does not enter a single character, they are repeatedly asked for a single character until one is entered.
# Then count the number of times the character appears in the sentence


sentence = input("Please, enter a sentence: ")
# deleted line
    singleCharacter = input("Please, enter a single character: ") 
    if len(singleCharacter) != 1:
        singleCharacter = input("Please, enter a single character: ") 
    else:
        break

characterCount = 0
for character in sentence:
    if character == singleCharacter:
# deleted line
print("The character", singleCharacter, "appears", characterCount, "times in the sentence", sentence, ".")
