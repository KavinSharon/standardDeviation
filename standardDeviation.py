import csv
import math
with open('pro/data.csv',newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

newData = []
for i in range(len(fileData)):
    noOfLines = fileData[i][0]
    newData.append(float(noOfLines))

n = len(newData)
total = 0
for x in newData:
    total = total+x

mean = total/n
print("The Mean Is "+str(mean))

squareList = []
for num in newData:
    a = int(num)-mean
    a = a ** 2
    squareList.append(a)

sum = 0
for a in squareList:
    sum = sum+a

div = sum/(len(newData)-1)
standardDeviation = math.sqrt(div)
print("The Standard Deviation is "+str(standardDeviation))