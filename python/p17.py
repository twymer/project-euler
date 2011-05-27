onesPlaceDict = {
	0: "",
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine" }

teensDict = {
	0: "ten",
	1: "eleven",
	2: "twelve",
	3: "thirteen",
	4: "fourteen",
	5: "fifteen",
	6: "sixteen",
	7: "seventeen",
	8: "eighteen",
	9: "nineteen" }

tensPlaceDict = {
	2: "twenty",
	3: "thirty",
	4: "forty",
	5: "fifty",
	6: "sixty",
	7: "seventy",
	8: "eighty",
	9: "ninety" }

result=0
for i in range(1000):
	currentNum =""
	currentNum += onesPlaceDict[int(i/100)]
	if int(i>=100):
		if(i%100==0):
			currentNum += " hundred "
		else:
			currentNum += " hundred and "
	if i%100 in range(10):
		currentNum += onesPlaceDict[i%100]
	elif i%100 in range(10,20):
		currentNum += teensDict[i%100-10]
	else:
		currentNum += tensPlaceDict[int(i/10)%10] + " " + onesPlaceDict[i%10]
	result+=len(currentNum.replace(" ",""))
	print(currentNum)
	print(len(currentNum.replace(" ","")))
result+=len("onethousand")
print(result)
