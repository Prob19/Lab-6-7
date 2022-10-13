"""Patrick Robinson
10/11/22
This code opens a text file and calculates the mean and median number of certain types of fruits eaten"""

import PatrickRobinsonStats #This imports data from my stats file



##this will parse the data
amountOfApplesEaten = []
amountOfBananasEaten = []
amountOfStrawberriesEaten = []
f= open("500DayFruitData.txt", "r") #This code opens ad reads the data in the text file
content=f.readlines()
for i in content: #These lines of code determine the amount of a certain type of fruit eaten depending on the name listed
	index= i.split()
	if index[1] == "apple":
		amountOfApplesEaten.append(int(index[2]))
	elif index[1] == "banana":
		amountOfBananasEaten.append(int(index[2]))
	elif index[1] == "strawberry":
		amountOfStrawberriesEaten.append(int(index[2]))

totalEaten = (amountOfApplesEaten + amountOfBananasEaten + amountOfStrawberriesEaten) #This line adds up the amount of each type of fruit eaten to get the total number eaten




newfile= open("Patrick_Robinson_output.txt","w") #These lines opens up a new text file and writes the following lines on it

newfile.write("The mean number of apples eaten is " + str(PatrickRobinsonStats.mean(amountOfApplesEaten)) + "\n")

newfile.write("The median number of apples eaten is " + str(PatrickRobinsonStats.median(amountOfApplesEaten)) + "\n")

newfile.write("The mode number of apples eaten is (are) " + str(PatrickRobinsonStats.mode(amountOfApplesEaten)) + "\n")

newfile.write("The mean number of bananas eaten is " + str(PatrickRobinsonStats.mean(amountOfBananasEaten)) + "\n")

newfile.write("The median number of bananas eaten is " + str(PatrickRobinsonStats.median(amountOfBananasEaten)) + "\n")

newfile.write("The mode number of bananas eaten is (are) " + str(PatrickRobinsonStats.mode(amountOfBananasEaten)) + "\n")

newfile.write("The mean number of strawberries eaten is " + str(PatrickRobinsonStats.mean(amountOfStrawberriesEaten)) + "\n")

newfile.write("The median number of strawberries eaten is " + str(PatrickRobinsonStats.median(amountOfStrawberriesEatenEaten)) + "\n")

newfile.write("The mode number of strawberries eaten is " + str(PatrickRobinsonStats.mode(amountOfStrawberriesEaten)) + "\n")

newfile.write("The mean number of total fruit eaten is " + str(PatrickRobinsonStats.mean(totalEaten)) + "\n")

newfile.write("The median number of total fruit eaten is " + str(PatrickRobinsonStats.median(totalEaten)) + "\n")

newfile.write("The mode number of total fruit eaten is (are) " + str(PatrickRobinsonStats.mode(totalEaten)) + "\n")



