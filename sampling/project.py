import pandas as pd
import statistics
import random
import plotly.figure_factory as ff

df = pd.read_csv('medium_data.csv')
f = 'reading_time'
data = df[f].tolist()

population_mean = statistics.mean(data)

def random_sets_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        randomindex = random.randint(0, len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], [f], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 100):
        mean_set = random_sets_of_mean(30)
        mean_list.append(mean_set)
    show_fig(mean_list)
    new_mean = statistics.mean(mean_list)
    print('Mean of population is: ', population_mean, 'Mean of sampling: ', new_mean)

setup()