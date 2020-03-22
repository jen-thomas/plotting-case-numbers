import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

def create_test_dataframe():
    data = [['2020-03-01', 'Spain', 150, 0], ['2020-03-02', 'Spain', 252, 2], ['2020-03-03', 'Spain', 400, 4],
            ['2020-03-01', 'Italy', 200, 0], ['2020-03-02', 'Italy', 250, 5], ['2020-03-03', 'Italy', 470, 10],
            ]

    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['Date', 'Country', 'Number of cases', 'Number of deaths'])
    df['Date'] = pd.to_datetime(df['Date'])

    # print dataframe.
    print(df)

    return df


def plot_dataframe_group_country(df):
    # Define colours of grouped points
    colours = {'Spain':'red', 'Italy':'blue'}

    # Create axes for plot
    fig, ax = plt.subplots(figsize=(8,6))

    # Group the data by country and plot the number of cases per day
    grouped = df.groupby('Country')
    for key, group in grouped:
        group.plot(ax=ax, kind='line', x='Date', y='Number of cases', label=key, color=colours[key])
    plt.show()
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of cases')

