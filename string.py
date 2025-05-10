#string formatting in python

letter = "Hey my name is {} and I am from {}"

names ="priyanka"
country  = "India"

print(f"Hey my name is {names} and I am from {country}") #output: Hey my name is priyanka and I am from India

price = 43.255554
txt = f"the price is {price:.2f}"
print(txt)



print(f"Hey my name is {{names}} and I am from {{country}}") #output: Hey my name is priyanka and I am from India


##doc string
def square(num):

    """
    This function returns the square of a number.
    """
    print(num**2)

square(4) #output: 16

print(square.__doc__) #output: This function returns the square of a number.
# print(square.__name__) #output: 



#PEP 8 - Python enhanced proposal
# 1. Use 4 spaces per indentation level.

import this