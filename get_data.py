#!/usr/bin/env python3

import csv
import sys


def get_data_for_countries(countries):
    countries_confirmed = {}
    countries_deaths = {}
    for country in countries:
        countries_confirmed[country] = get_data('data/time_series_19-covid-Confirmed.csv', country)
        countries_deaths[country] = get_data('data/time_series_19-covid-Deaths.csv', country)

    confirmed_and_deaths = merge(countries_confirmed, countries_deaths)

    return confirmed_and_deaths


def countries_population():
    # From Wikipedia
    return {'Spain': 46_733_038,
            'United Kingdom': 67_454_757,
            'Switzerland': 8_570_146,
            'Italy': 60_317_546,
            'US': 328_239_523,
            'Germany': 83_149_300,
            'China': 1_427_647_786
            }


def get_data(file_path, country):
    output = []
    with open(file_path) as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for country_information in csv_reader:
            if country_information['Country/Region'] == country:
                output = process_country(country_information)

    return output


def process_country(country_information):
    result = {}

    reading = False
    for key, items in country_information.items():
        if key == '1/22/20':
            reading = True

        if reading:
            result[key] = items

    return result


def merge(confirmed, deaths):
    output = []
    for country, country_confirmed in confirmed.items():
        for date in country_confirmed:
            output.append([country, date, confirmed[country][date], deaths[country][date]])

    return output


def print_confirmed_deaths_rate(confirmed_and_deaths):
    previous_confirmed = previous_deaths = 0
    for item in confirmed_and_deaths:
        date, confirmed, deaths = item
        confirmed = int(confirmed)
        deaths = int(deaths)

        if previous_confirmed == 0:
            rate_confirmed = None
        else:
            rate_confirmed = f'{confirmed / previous_confirmed:.2f}'

        if previous_deaths == 0:
            rate_deaths = None
        else:
            rate_deaths = f'{deaths / previous_deaths:.2f}'

        print(f'{date}\t{confirmed}\t{deaths}\t{rate_confirmed}\t{rate_deaths}')

        previous_confirmed = confirmed
        previous_deaths = deaths


if __name__ == '__main__':
    print(get_data_for_countries(['Spain', 'Italy']))
    sys.exit(1)
