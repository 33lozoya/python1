# Write a currency conversion program that first asks the user to type in today’s price (rate) of one euro in Japanese Yen, i.e. the yen rate (approximately 131.96 yen).
# The program should then ask the user to input a euro amount and while the euro amount entered is not 0 the loop should convert the euro amount to the Japanese yen equivalent and print the yen value for each.
# The loop will continue to read in another euro amount and convert it until the user enters 0 as the euro amount.

yen = float(input("Please, enter today's Japanese Yen rate for one Euro: "))

while True:
    euro = float(input("Please, enter the amount in Euros (press 0 to exit): "))
    if euro != 0:
        yen = euro * yen
        print("The equivalent Yen amount is: ", yen)
    else:
# deleted line
