"""Patrick Robinson
10/11/22
This file contains the functions that calculate the mean and median of the fruit text file"""

f= open("500DayFruitData.txt", "r") #This code opens the text file and reads the data inside of it
content=f.read()



def mean(listOfNums): #This code code calculates the mean of a list and rounds it to 2 decimal spaces
	sumofnumbers = 0
	for num in listOfNums:
		sumofnumbers += int((num))
		
	meanoflist = sumofnumbers / len(listOfNums)
	return round(meanoflist,2)



def median(num): #This code calculates the median of a list and rounds it to 2 decimal spaces
	num.sort() #This sorts the list from least to greatest.
	if (len(num) % 2 == 0):
		firstIndex = int((len(num))/2)-1
		secondIndex= firstIndex +1
		firstNumber= num[firstIndex]
		secondNumber= num[secondIndex]
		median= (firstNumber + secondNumber) /2 
		
	else:
		index = (len(num)//2)
		median = num[index]
	return round(median, 2)
modeoflist=()		
def mode(num): #This code calculates the mode using dictionarys
	mydict={}
	max_mode = 0
	myList = []
	for i in num:
		if i in mydict:
			mydict[i] += 1
		else:
			mydict[i] = 1
	for j in mydict.values():
		if j > max_mode:
			
			max_mode = j
	for k in mydict.keys():
		if mydict[k] == max_mode:
			myList.append(k)
	

