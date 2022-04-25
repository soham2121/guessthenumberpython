import csv
from math import sqrt

with open('data.csv') as f:
    reader = csv.reader(f)
    data_list = list(reader)
    data = data_list[0]

def findmean(data):
    number = len(data)
    total = 0

    for x in data:
        total += int(x)

    mean = total/number
    return mean

squarednum = []
for x in data:
    a = int(x) - findmean(data)
    a = a**2
    squarednum.append(a)

sum = 0
for x in squarednum:
    sum += x

num = sum/(len(data) - 1)

final = sqrt(num)

print('The final number is: ', final)