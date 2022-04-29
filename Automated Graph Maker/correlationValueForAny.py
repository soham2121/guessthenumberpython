import csv
import numpy as np
import pandas as pd
import plotly.express as px

def plotGraph(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = x, y = y)
        fig.show()

def getData(data_path):
    x_data = []
    y_data = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            x_data.append(float(row[x]))
            y_data.append(float(row[y]))

    return {'x_values': x_data, 'y_values': y_data}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x_values'], data_source['y_values'])
    print('The correlation between', x, 'and', y, 'is:', correlation[0,1])

data_path = input('Enter The File Name: ')
x = input('Enter The X Value: ')
y = input('Enter The Y Value: ')
data_source = getData(data_path)
findCorrelation(data_source)
plotGraph(data_path)