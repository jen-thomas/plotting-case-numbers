#!/bin/bash

# Data from: https://github.com/CSSEGISandData/COVID-19

wget "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv" -O data/time_series_19-covid-Confirmed.csv
wget "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv" -O data/time_series_19-covid-Deaths.csv
