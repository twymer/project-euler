# Problem 21
import math

def calcProperSum(x):
  result=0
  for i in range(1, int(math.sqrt(x)+1)):
    if x%i == 0:
      #print(i)
      #print(x/i)
      result+=i
      result+=x/i
  return result-x

properSum={}
result=0
for i in range(10000):
  if i not in properSum:
    properSum[i] = calcProperSum(i)
    temp = properSum[i]
    if temp not in properSum:
      properSum[temp] = calcProperSum(temp)
    if temp < 10000 and i == properSum[temp] and i != temp:
      result+=i
print(result)
