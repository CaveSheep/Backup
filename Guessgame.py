import random

mysteryNum = random.randint(1, 100)
score = 0

while True:
	guess = int(input("Pick a number between 1 to 100: "))
	score = score + 1

	if guess == mysteryNum:
		print("Very Niceu")
		break

	elif guess > mysteryNum:
		print("c'mon man, too high")
	else:
		print("Really? Go higher")

print("It took you " + str(score) + " guesses")







