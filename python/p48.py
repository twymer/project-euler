#This seems lame, but it's extremely fast in python...
result=0
for i in range(1,1001):
    result+=i**i
result=str(result)
print(result[-10:])
