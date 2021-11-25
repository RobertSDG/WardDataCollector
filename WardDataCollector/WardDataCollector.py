""" File to collect data from opendata.bristol api in a format that can be uploaded
    to the open data platform
"""

import sys
import csv
from urllib.parse import urlencode

import requests


# Function accepts a dictionary and parses out the data to a array and returns
# the array with the corrections. We do not want to include the name bristol
# as that will force the platform to treat it as a headine indicator
def parse_data(req_data):
    for field in req_data:
        if field[0] == ".Bristol Average":
            field[0] = ""
    return req_data

# Function to build the URL to query the Open Data API
def build_url(dataset, refine_indicator):
    get_vars = {'dataset': dataset, 'rows': 50, 'refine.indicator': refine_indicator}
    base_url = "https://opendata.bristol.gov.uk/api/records/1.0/search/?"
    uri = base_url + urlencode(get_vars)
    print(uri)
    #requests.get(uri)
    return uri

# throws a excception on connection failed, this should be handled externally to retry after delay
def get_data(url):
    response = requests.get(url)
    print(response.status_code)

    #results should be appended in order Ward, GeoCode, value
    result = []
    if response.status_code == 200:
        # parse json
        body = response.json()['records']
        # print(body);
        for row in body:
            ptr = row['fields']
            if "ward_code" in ptr:
                res = [ptr['ward_name'], ptr['ward_code'], ptr['statistic']]
            else:
                res = [ptr['ward_name'], "", ptr['statistic']]
            result.append(res)
            # print(res)

            #print(x)
    return result

def data_to_csv(collection, file_name):
    #instantiate_file
    with open(file_name + '.csv', mode='w') as employee_file:
        data_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # write headers
        data_writer.writerow(['Year', 'Ward', 'GeoCode','Value'])
        # for each set of data
        for key in collection:
            # for each row (containing ward)
            for item in collection[key]:
                row = item
                #add date to front of row
                row.insert(0, key)
                data_writer.writerow(row)


    return

# Main entry for script
def main():
    # URL = "https://opendata.bristol.gov.uk/api/records/1.0/search/?
    # dataset=quality-of-life-2018-19-ward&
    # refine.indicator=%25+satisfied+with+their+local+area"
    dataset_year = [
        "2017-18",
        "2018-19",
        "2019-20",
        "2020-21"
        ]
    dataset = "quality-of-life-2018-19-ward"
    indicator = "% satisfied with their local area"
    url = build_url(dataset, indicator)
    response = get_data(url)
    datasets = {}

    for row in dataset_year:
        template = f'quality-of-life-{row}-ward'
        print(template)
        url = build_url(template, indicator)
        response = get_data(url)
        datasets[row]=response

    # print(datasets)

    for key in datasets:
        datasets[key] = parse_data(datasets[key])
    print(datasets)

    data_to_csv(datasets, indicator)
    #print (unity)
    #fetch = requests.get(URL)
    #print(fetch.status_code)
    #print(fetch.json())
    return 0

if __name__ == "__main__":
    sys.exit(int(main() or 0))
