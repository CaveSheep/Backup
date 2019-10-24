# Calculation, printing, variables

# Printing to the screen 
# The built in function print(), prints to the screen
# It will print both Strings and numbers
print("printing to the screen...")
print("hello") # a string
print('hello again')
print(6) # a number
print("6") # a string again
print(6 + 6)
print("6" + "6") # string concatenation
print("6" + (6)) # Error, but with str it works
# Performing calculations
# adding +
# subtracting -
# multiply *
# division /
# exponents **
# module %

print(4-2)
print(4 * 2)
print(4 ** 2)
print(4/3)
print("Modulo operator test...") # gives remainders
print(5 % 3)
print(10 % 2)
print(16 % 3)

badLuck = 13
print("badLuck = " + str(badLuck))
goodLuck = "4"
print("goodLuck =" + goodLuck)
badLuck + 5
print(badLuck)
badLuck = badLuck + 5
print(badLuck)

name = input("What is your name? ")
print("Hello" + name)
print(name * 10)
name = name + "\n"
print(name * 10)
base = input("Enter the base number: ")
exp = input("Enter the exponent: ")
print(int(base) ** int(exp))