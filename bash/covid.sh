#!/bin/bash
# This scropt downloads covid data and displays it


positive=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].positive')
today=$(date)
data=$(curl https://api.covidtracking.com/v1/us/ecurrent.json)

negative=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].negative')
death=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].death')

hospitalized=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].hospitalized')



echo "On $today, there were $positive positive COVID cases, $negative negative tests, $death deaths, and $hospitalized in the hospital." 

