import time
import os

name = input("What is your name? ")
print("Yo, " + name, "Time to play some hangman")

myWord = "hello"

choice = input("Type a word: ")

if choice == myWord:
	print("Wow, you cheater")
else:
	print("Pffft, you suck lol")

letter = input("Enter a letter: ")

if letter in myWord:
	print("You got one")
else:
	print("Aww, try again")

count = 0

for letter in myWord:
	if letter == choice:
		print(count)
	count += 1

myString = "Arizona"
mysteryWord = list(myString)
print(mysteryWord)
guessList = []

for letter in mysteryWord:
	guessList.append("_")

print(guessList)

guessList[3] = "z"

print(guessList)