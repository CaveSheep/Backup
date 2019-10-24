age = input("How old are you? ") # prompt for age

# check if age is more than 17, so the person can see R rated movie alone
age = int(age)

if age >= 17: 
	print("You can see an R rated movie")

else:
	print("Sorry bud, but no movie for you")

print("Have a nice day")

birthday = input("Is today your birthday (yes or no)? ")
if birthday == "yes":
	print("Cool")

print("Ok, now go away")

myNum = 7 
guess = input("Guess a number between 1 to 10? ")
if guess == myNum:
	print("Lucky")
elif guess > myNum:
	print("Oof")
else:
	print("Oof")
print("Thanks for letting me waste your time")	