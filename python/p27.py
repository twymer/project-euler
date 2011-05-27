#Change to use b being only prime
#is not my original idea, was written
#after the fact.
import math

def isPrime(num):
	if num<0 or num%2==0:
		return False
	for i in range(3,int(math.sqrt(num)+1),2):
		if num%i==0:
			return False
	return True

maxCoefs=0
maxLength=0
for a in range(-999,1000):
	for b in range(0,1000):
		if isPrime(b):
			n=0
			while isPrime(n*n+a*n+b):
				n+=1
			if n>maxLength:
				maxLength=n
				maxCoefs=a*b
				print("a:",a,"b:",b)
print(maxCoefs)
