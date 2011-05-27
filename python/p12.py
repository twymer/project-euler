# Problem 12
import math
triangle=0
i=1
while True:
    #print(triangle)
    triangle+=i
    i+=1
    count=0
   # j=1
    for j in range(1,int(math.sqrt(triangle))):
        #if i>triangle:
        #    break
        if triangle%j==0:
            count+=2
        j+=1
    if count>499:
        print("winner:",triangle)
        break
