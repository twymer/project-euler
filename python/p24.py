a=[0,1,2,3,4,5,6,7,8,9]
test1=[0,1,2]
test2=[0,2,1]
test3=[1,2,0]
#a=test1

count=0
test=True
while count<1000000-1:
    if count%100000==0:
        print(count)
    #if count>999995:
    #    print(a)
    #print(a)
    pos=-1
    for i in range(len(a)-1):
        if a[i]<a[i+1]:
#            print("found",a[i])
            pos=i
    smallestVal=99
#    print("a[pos]=",a[pos])
#    print("pos=",pos)
    for i in range(pos, len(a)):
        if a[i]>a[pos] and a[i]<smallestVal:
            smallestVal=a[i]
    if pos==-1:
        break
#    print("smallestVal=",smallestVal)
    temp = a.pop(a.index(smallestVal))
    a.insert(pos,temp)
    #sort remainder
    temp2 = []
    #print("pos=",pos)
    for i in range(pos,len(a)-1):
        #print(i)
        temp2.append(a.pop())
    temp2.sort()
#    print("temp2=",temp2)
    a.extend(temp2)
    count+=1
    
print(a)
        

##    print("pos",pos)
##    for i in range(len(a)-1,pos,-1):
##        #print("2nd")
##        print(a[i],"<?",a[pos])
##        if a[i]<a[pos+1]:
##            temp = a.pop(pos+1)
##            a.insert(i,temp)
##            break
##    print('')
##    
        
        

##i=len(a)-1
##for junk in range(6):
##    print(a)
##    largest=-1
##    print("i",i)
##    for j in range(i-1,-1,-1):
##        print(a[j],"<?",a[i])
##        if a[j]<a[i] and (largest<0 or a[j]>a[largest]):
##            largest=j
##    print("largest",largest)
##    if largest >= 0:
##        temp = a.pop(i)
##        print("popped", temp)
##        a.insert(largest,temp)
##        i=len(a)-1
##    else:
##        print("keep going")
##        i-=1
##    count+=1
##    print('')
