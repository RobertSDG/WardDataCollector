# File to collect data from opendata.bristol api in a format that can be uploaded to the open data platform

import sys
import csv as csv
import requests

# url for the open Data Platform
URL = "https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=quality-of-life-2018-19-ward&refine.indicator=%25+satisfied+with+their+local+area"


def main(): 
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))
