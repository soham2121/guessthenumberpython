import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv('students.csv')
data_list = df['math score'].to_list()

mean = statistics.mean(data_list)
median = statistics.median(data_list)
mode = statistics.mode(data_list)
stdev = statistics.stdev(data_list)

print("Mean, Median and Mode of height is {}, {} and {} respectively".format(mean, median, mode))
print("Standard deviation: ", stdev)

first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2 * stdev), mean + (2 * stdev)
third_stdev_start, third_stdev_end = mean - (3 * stdev), mean + (3 * stdev)

data_within_1_deviation = [result for result in data_list if result > first_stdev_start and result < first_stdev_end]
data_within_2_deviation = [result for result in data_list if result > second_stdev_start and result < second_stdev_end]
data_within_3_deviation = [result for result in data_list if result > third_stdev_start and result < third_stdev_end]

print("{}% of data for height lies within 1 standard deviation".format(len(data_within_1_deviation)*100.0/len(data_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(data_within_2_deviation)*100.0/len(data_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(data_within_3_deviation)*100.0/len(data_list)))

fig = ff.create_distplot([data_list], ["Result"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = 'lines', name = 'mean'))
fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.17], mode = 'lines', name = 'stdev 1'))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.17], mode = 'lines', name = 'stdev 1'))
fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.17], mode = 'lines', name = 'stdev 2'))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.17], mode = 'lines', name = 'stdev 2'))
fig.add_trace(go.Scatter(x = [third_stdev_start, third_stdev_start], y = [0, 0.17], mode = 'lines', name = 'stdev 3'))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.17], mode = 'lines', name = 'stdev 3'))
fig.show()