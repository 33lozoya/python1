# Create a program that calculates a Fibonacci sequence.
# A Fibonacci sequence is characterized by the fact that every number after the first two is the sum of the two preceding ones.
# The user will enter the number of terms, and you must display the sequence using a for loop, include error checking to ensure the number is at least one.

terms = (int(input("Please, enter the number of terms in the Fibonacci sequence: ")))

fibonacciSequence = [1, 1]

for num in range(2, terms):
# line deleted
    fibonacciSequence.append(nextTerm)

print("The Fibonacci sequence up to", terms, "terms is:")
for term in fibonacciSequence:
    print(term)
