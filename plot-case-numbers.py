import pandas as pd
import matplotlib.pyplot as plt
import get_data

def create_test_dataframe():
    data = [['Spain', '2020-03-01', 150, 0], ['Spain', '2020-03-02', 252, 2], ['Spain', '2020-03-03', 400, 4], \
           ['Italy', '2020-03-01', 200, 0], ['Italy', '2020-03-02', 250, 5], ['Italy', '2020-03-03', 470, 10],
    ]

    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['Date', 'Country', 'Number of cases', 'Number of deaths'])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Number of cases'] = pd.to_numeric(df['Number of cases'])
    df['Number of deaths'] = pd.to_numeric(df['Number of deaths'])

    # print dataframe.
    print(df)

    return df


def put_data_list_into_dataframe(data_list):

    df = pd.DataFrame(data_list, columns=['Country', 'Date', 'Number of cases', 'Number of deaths'])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Number of cases'] = pd.to_numeric(df['Number of cases'])
    df['Number of deaths'] = pd.to_numeric(df['Number of deaths'])

    return df


def find_proportion_new_cases(df):

    pass


def plot_dataframe_group_country(df):
    # Define colours of grouped points
    colours = {'Spain':'red', 'Italy':'blue'}

    # Create axes for plot
    fig, ax = plt.subplots(figsize=(8,6))

    # Group the data by country and plot the number of cases per day
    df['delta_Number of cases'] = df.groupby('Country')['Number of cases'].diff()

    df['delta_Number of cases_per_milion'] = df.groupby('Country')['']

    df['ratio_Number of cases'] = df['delta_Number of cases'].div(df.groupby('Country')['delta_Number of cases'].shift(1))
    grouped = df.groupby('Country')
    for key, group in grouped:
        #group.plot(ax=ax, kind='line', x='Date', y='Number of cases', label=key, color=colours[key])
        #group.plot(ax=ax, kind='line', x='Date', y='delta_Number of cases', label=key, color=colours[key])
        group.plot(ax=ax, kind='line', x='Date', y='ratio_Number of cases', label=key, color=colours[key])

    ax.set_xlabel('Date')
    ax.set_ylabel('Number of cases')

    plt.show()


if __name__ == '__main__':

    data_list = get_data.get_data_for_countries(['Spain', 'Italy'])
    #data_list = [['Spain', '2020-03-01', 150, 0], ['Spain', '2020-03-02', 252, 2], ['Spain', '2020-03-03', 400, 4], \
    #        ['Italy', '2020-03-01', 200, 0], ['Italy', '2020-03-02', 250, 5], ['Italy', '2020-03-03', 470, 10],
    #        ]
    df = put_data_list_into_dataframe(data_list)

    plot_dataframe_group_country(df)
