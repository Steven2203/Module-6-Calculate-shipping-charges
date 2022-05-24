#-------------------------------------------------------------------------------
# Name:        module 6 - Schipping charges calculator
# Purpose:     Calculate shipping charges for a shopper
# Author:      Steven
# Created:     24-05-2022
# Copyright:   (c) Steven 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##Ask the user to enter the total amount of $

shippingCost = 10
shippingCost = float(shippingCost)
totalSpend = input("Enter the total amount spend")
totalSpend = int(totalSpend)

##Using conditionals in my code to make right decisions.
##Had to use formatted string to concatenate different datatypes.
##Luckilly i am using Python 3 :)

if float(totalSpend) >= 50:
    message = f'The total amount is : {totalSpend}'
    print(message)
    ##OLD: print("The total amount is: " + totalSpend)
elif float(totalSpend) < 50:
    messageShipping = f'The total amount including shipping is: {totalSpend} + {shippingCost} '
    print(messageShipping)
    ##OLD: print("The total amount including shipping is: " + totalSpend + shippingCost)
else:
    print("You did not enter a valid number")

##Converting the variables to floats and printing out the final calculation.

totalSpend == float
shippingCost == float
totalCalculation = totalSpend + shippingCost
print("The final calculation is:")
print(totalCalculation)
