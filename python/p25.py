fibNMinus2=1
fibNMinus1=1
fibN=2
count=3
while len(str(fibN))<1000:
    count+=1
    fibNMinus2=fibNMinus1
    fibNMinus1=fibN
    fibN=fibNMinus2+fibNMinus1
print(count)
