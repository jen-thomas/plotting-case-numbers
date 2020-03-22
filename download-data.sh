#!/bin/bash

# Data from: https://github.com/CSSEGISandData/COVID-19

wget "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv" -O data/time_series_19-covid-Confirmed.csv
wget "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv" -O data/time_series_19-covid-Deaths.csv
