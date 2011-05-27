# Problem 19
# Research used for this question:
#   January 1st 1901 is a Tuesday
has30 = [9,4,5,11]
days=0
count=0
for year in range(1901,2000):
    for i in range(1,13):
        if days%7==6:
            count+=1
        if i in has30:
            days+=30
        elif i == 4:
            if isLeapYear(year):
                days+=29
            else:
                days+=28
        else:
            days+=31
print(count)

def isLeapYear(year):
    if year%400 == 0:
        return true
    if year%100 == 0:
        return false
    if year%4 == 0:
        return true
