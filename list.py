favFoods = ["Pie", "Ice", "Ramen"]

print(favFoods[0])
print(favFoods[2])
print(favFoods[1])
# adds to the end of the list
favFoods.append("Yogurt")
print(favFoods)
print(favFoods[3])
print("My 4th fav food is " + favFoods[3])
favFoods.insert(1, "Steak")
print(favFoods)
favFoods.remove("Ice")
print(favFoods)
favFoods.pop(0)
print(favFoods)

for food in favFoods:
	print(food)

numList = [3, 6, 2, 10, 22, 44, 53, 7]

sum = 0
for num in numList:
	sum = sum + num
print(sum)

print(len(numList))

myfood = input("What is your favorite food? ")
favFoods.append(myfood)
print(favFoods)
print(favFoods[len(favFoods)-1])

mov = ["Spiderman", "Spiderman 2", "Spiderman 3", "Homecoming", "Far From Home", "Spiderverse", "Amazing", "Amazing 2"]
mymov = input("What is your favorite your favorite spiderman movie? ")