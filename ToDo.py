print("Welcome to your To Do List since you can't remember things yourself.")
todoList = []
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print/review your list")
	print("Enter q to get the flip out of there")
	choice = input("Choose now or else: ")

	if choice == "q":
		print("lol, ok bye")
		break
	elif choice == "a":
		a = input("What would you like to add? ")
		todoList.append(a)
		pass
	elif choice == "r":
		r = input("What would you like to banish? ")
		todoList.remove(r)
		pass
	elif choice == "p":
		print(str(todoList))
		pass
	else:
		print("Sorry, but this is not how you use this. Try Again")
		pass

