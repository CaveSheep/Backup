import random

wordList = ["doctor mario", "sonic", "diddy kong", "bowser jr", "falco", "yoshi", "robin", "mr game and watch", "pikachu", "duck hunt", "kirby", "pichu", "olimar"] 
name = input("What is your name? ")
print("Yo " + name, " time to play some hangman")

mysteryWord = random.choice(wordList)

guessList = []

for letter in mysteryWord:
	guessList.append("_")

print(guessList)

while True:
	letter = input("Type in a letter: ")
	if letter == mysteryWord:
		print("Nice, you got it")
	else:
		print("Try again,")
		count += 1
		print(count)




