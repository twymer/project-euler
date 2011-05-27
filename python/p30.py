result=0
for n in range(10,1000000):
	tempSum=0
	for digit in str(n):
		tempSum+=int(digit)**5
	if n == tempSum:
		result+=n
print(result)
