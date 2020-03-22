import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

data = [['2020-03-01', 'Spain', 10, 0], ['2020-03-02', 'Spain', 25, 2], ['2020-03-03', 'Spain', 40, 4],
        ['2020-03-01', 'Italy', 20, 0], ['2020-03-02', 'Italy', 50, 5], ['2020-03-03', 'Italy', 70, 10],
        ]

# Create the pandas DataFrame 
df = pd.DataFrame(data, columns=['Date', 'Country', 'Number of cases', 'Number of deaths'])
df['Date'] = pd.to_datetime(df['Date'])

# print dataframe. 
print(df)


# Define colours of grouped points
colors = {'Spain':'red', 'Italy':'blue'}

# Create axes for plot
fig, ax = plt.subplots(figsize=(8,6))

# Group the data by country and plot the number of cases per day
grouped = df.groupby('Country')
for key, group in grouped:
    group.plot(ax=ax, kind='line', x='Date', y='Number of cases', label=key, color=colors[key])
plt.show()

