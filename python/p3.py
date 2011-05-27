# Problem 3
import math
bigNum=600851475143 
for i in range(int(math.sqrt(bigNum)), 1, -1):
    if bigNum%i==0:
        if i%2!=0:
            for j in range(3,int(math.sqrt(i))+1,2):
                if i!=j and i%j==0:
                    #print("Number",i,"failed the test on",j)
                    break
            else: #prime
                print("winner:",i)
                break
