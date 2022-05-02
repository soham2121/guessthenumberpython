import csv
from typing import Counter

with open('heightandweight.csv') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    file_data.pop(0)

data = []
for i in range(len(file_data)):
    num = file_data[i][2]
    data.append(float(num))

length = len(data)
sum = 0
for num in data:
    sum += num
mean = sum/length
print('Mean (Average) is -> ', mean)

data.sort()
if length % 2 == 0:
    midvalue1 = float(data[length//2])
    midvalue2 = float(data[length//2-1])
    median = (midvalue1 + midvalue2)/2
else:
    median = float(data[length//2])
print('Median is -> ', median)

newdata = Counter(data)
data_range = {
    '90 - 99': 0,
    '100 - 109': 0,
    '110 - 119': 0,
    '120 - 129': 0,
    '130 - 139': 0,
    '140 - 149': 0,
    '150 - 159': 0
}
for weight,occurence in newdata.items():
    if 90 <= float(weight) < 100:
        data_range['90 - 99'] += occurence
    if 100 <= float(weight) < 110:
        data_range['100 - 109'] += occurence
    if 110 <= float(weight) < 120:
        data_range['110 - 119'] += occurence
    if 120 <= float(weight) < 130:
        data_range['120 - 129'] += occurence
    if 130 <= float(weight) < 140:
        data_range['130 - 139'] += occurence
    if 140 <= float(weight) < 150:
        data_range['140 - 149'] += occurence
    if 150 <= float(weight) < 160:
        data_range['150 - 159'] += occurence

mode = data_range['90 - 99']
mode_name = ''
for i in data_range:
    if data_range[i] > mode:
        mode = data_range[i]
        mode_name = i
print('Mode is -> ', mode_name)