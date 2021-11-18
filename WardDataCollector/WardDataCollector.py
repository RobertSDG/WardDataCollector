# File to collect data from opendata.bristol api in a format that can be uploaded to the open data platform

import sys
import csv as csv
import requests

# url for the open Data Platform

def main():
    URL = "https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=quality-of-life-2018-19-ward&refine.indicator=%25+satisfied+with+their+local+area"
    
    fetch = requests.get(URL)
    print(fetch.status_code)
    print(fetch.json())
    return

if __name__ == "__main__":
    sys.exit(int(main() or 0))

# Function accepts a json object from request and parses out the data to a array and returns
# the array
def parse_data(Json):

    pass