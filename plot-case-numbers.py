import matplotlib.pyplot as plt
import pandas as pd

import get_data


def create_test_dataframe():
    data = [['Spain', '2020-03-01', 150, 0], ['Spain', '2020-03-02', 252, 2], ['Spain', '2020-03-03', 400, 4], \
            ['Italy', '2020-03-01', 200, 0], ['Italy', '2020-03-02', 250, 5], ['Italy', '2020-03-03', 470, 10],
            ]

    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=['Country', 'Date', 'Number of cases', 'Number of deaths'])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Number of cases'] = pd.to_numeric(df['Number of cases'])
    df['Number of deaths'] = pd.to_numeric(df['Number of deaths'])

    print(df)

    return df


def calculate_number_of_cases_per_million(row):
    return 1_000_000 * (row['delta_Number of cases'] / get_data.countries_population()[row['Country']])


def put_data_list_into_dataframe(data_list):
    df = pd.DataFrame(data_list, columns=['Country', 'Date', 'Number of cases', 'Number of deaths'])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Number of cases'] = pd.to_numeric(df['Number of cases'])
    df['Number of deaths'] = pd.to_numeric(df['Number of deaths'])

    return df


def find_proportion_new_cases(df):
    df['New daily cases'] = df.groupby('Country')['Number of cases'].diff()
    df['New daily deaths'] = df.groupby('Country')['Number of deaths'].diff()

    df['Ratio new cases'] = df.groupby('Country')['New daily cases'].pct_change() + 1
    df['Ratio new deaths'] = df.groupby('Country')['New daily deaths'].pct_change() + 1

    return df


def cases_per_million_population(df):
    df['delta_Number of cases'] = df.groupby('Country')['Number of cases'].diff()

    df['delta_Number of cases_per_million'] = df.apply(calculate_number_of_cases_per_million,
                                                       axis=1)

    df['ratio_Number of cases'] = df['delta_Number of cases'].div(df.groupby('Country')['delta_Number of cases'].shift(1))

    return df


def plot_new_cases_group_country(df):
    colours = {'Spain': 'red', 'Italy': 'green', 'United Kingdom': 'blue'}

    # Create axes for plot
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    ax11 = ax1.twinx()
    ax22 = ax2.twinx()

    # Group the data by country and plot the number of cases per day
    grouped = df.groupby('Country')
    for key, group in grouped:
        group.plot(ax=ax1, kind='line', x='Date', y='Number of cases', label=key, color=colours[key])
        group.plot(ax=ax11, kind='line', linestyle='--', x='Date', y='Ratio new cases', label=key, color=colours[key])
        group.plot(ax=ax2, kind='line', x='Date', y='delta_Number of cases', label=key, color=colours[key])
        group.plot(ax=ax22, kind='line', linestyle='--', x='Date', y='delta_Number of cases_per_million', label=key, color=colours[key])

    # Plot a horizontal line where the ratio of new daily cases is 1
    ax11.axhline(y=1, color='lightgrey', linestyle='-')

    ax1.set_xlabel('Date')
    ax1.set_ylabel('Number of cases')
    ax11.set_ylabel('Ratio of new daily cases')

    ax2.set_xlabel('Date')
    ax2.set_ylabel('Number of cases per million?')
    ax22.set_ylabel('Delta number of cases per million?')

    plt.show()


if __name__ == '__main__':
    data_list = get_data.get_data_for_countries(['Spain', 'Italy', 'United Kingdom'])

    df = put_data_list_into_dataframe(data_list)

    df = find_proportion_new_cases(df)
    df = cases_per_million_population(df)

    plot_new_cases_group_country(df)