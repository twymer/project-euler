# Problem 10
# Old solution, uses slow slow prime check..
import math
x=2;
for i in range(3, 2000000):
    if i%100000==0: print(i)
    if i%2!=0:
        for j in range(3,int(math.sqrt(i))+1,2):
            if i!=j and i%j==0:
                #print("Number",i,"failed the test on",j)
                break
        else:
            #print("prime:",i)
            x+=i
print(x)
