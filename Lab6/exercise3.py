# Write a program that sums all the odd numbers between 1 and 20 inclusively and also sums the even numbers between 1 and 20 in the same loop. 
# Print both results. Desk check your resulting answers.

odd = 0
even = 0

# deleted line
    if number % 2 == 0:
        even += number
    else:
        odd += number

print("Sum of even numbers: ", even)
print("Sum of odd numbers: ", odd)
