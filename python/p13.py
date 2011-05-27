# Problem 13
# I dislike this solution very much :-P
import math
import io
file = io.open("p13input.txt","r")
result=0
for i in range(100):
    result+=int(file.readline().strip())
