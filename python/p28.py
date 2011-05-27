#Instant
#TODO: less looping, look at each diagonal individually
result=1
currentNum=1
for layer in range(1,501):
	for corner in range(4):
		currentNum+=layer*2
		result+=currentNum
print(result)
