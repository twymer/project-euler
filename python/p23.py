import math
abundantNumbers=set()
abundantSums=set()

def calcProperSum(x):
    result=0
    for i in range(1,int(x/2+1)):
        if x%i == 0:
            result+=i
            #result+=x/i
    return result

def populateAbundants():
    for i in range(1,28123):
        if i%1000==0:
            print(i)
        if calcProperSum(i)>i:
            abundantNumbers.add(i)
    #return len(abundantNumbers)
            

result=0
populateAbundants()
print("populated")
for x in abundantNumbers:
    for y in abundantNumbers:
        if x+y>28123:
            break
        if x+y not in abundantSums:
            abundantSums.add(x+y)
for i in range(28123):
    if i not in abundantSums:
        result+=i
        print(i)
            

print(result)
##
##result=0
##for i in range(1,28123):
##    if i%100==0:
##        print(i)
##    test=True
##    for j in range(0,math.ceil(i/2)):
##        if isAbundant(i-j) and isAbundant(j):
##            #print(i-j)
##            #print(j)
##            #print("")
##            test=False
##            break
##    if test:
##        result+=i
##            
