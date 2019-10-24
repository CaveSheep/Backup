import random

wordList = ["doctormario", "sonic", "diddykong", "bowserjr", "falco", "yoshi", "robin", "mrgameandwatch", "pikachu", "duckhunt", "kirby", "pichu", "olimar", "megaman", "chibirobo"] 
name = input("What is your name? ")
print("Yo " + name, " time to play some hangman")

mysteryWord = random.choice(wordList)

guessList = []

for letter in mysteryWord:
	guessList.append("_")

print(guessList)


#while True:
#	letter = input("Type in a letter: ")
#	if letter == mysteryWord:
#		print("Nice, you got it")
#	else:
#		print("Try again,")
#		count += 1
#		print(count)



while True:
	count = 0
	guess = input("Guess a letter: ")
	if guess in mysteryWord:
		print("You got it!")
		for letter in mysteryWord:
			if letter == guess:
				guessList[count] = guess
			count += 1
			print(guessList)
