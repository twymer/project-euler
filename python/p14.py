# Problem 14
maxCount=0
foundAt=0
for i in range(1000000):
    if i%10000==0: print(i)
    count=0
    x=i
    while x>1:
        if x%2==0:
            x=x/2
        else:
            x=3*x+1
        count+=1
    if count>maxCount:
        maxCount=count
        foundAt=i
print("winner:",foundAt,"containing",maxCount,"iterations")
