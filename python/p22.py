# Problem 22
result=0
file = open("names.txt","r")
line = file.readline()
names = line.replace("\"",'').split(",")
names.sort()
for i in range(len(names)):
    score=0
    for char in names[i]:
        score+=(ord(char)-64)
    result+=score*(i+1)
print(result)
file.close()
