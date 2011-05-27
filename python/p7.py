# Problem 7
# http://projecteuler.net/index.php?section=problems&id=7
import math
x=0;
for i in range(3, 2000000):
    if x%1000==0: print(x)
    if i%2!=0:
        for j in range(3,int(math.sqrt(i))+1,2):
            if i!=j and i%j==0:
                #print("Number",i,"failed the test on",j)
                break
        else:
            #print("prime:",i)
            x+=1
            if x == 10000:
                print("winner:",i)
                break
#print(x)
