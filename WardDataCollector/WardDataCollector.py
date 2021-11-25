# File to collect data from opendata.bristol api in a format that can be uploaded to the open data platform

import sys
import csv as csv
import requests
from urllib.parse import urlparse, urlencode

# Function accepts a json object from request and parses out the data to a array and returns
# the array
def parse_data(Json):

    pass


def buildUrl(dataset, refineIndicator):
    getVars = {"dataset": dataset, "rows": 50, "refine.indicator": refineIndicator}
    baseUrl = "https://opendata.bristol.gov.uk/api/records/1.0/search/?"
    uri = baseUrl + urlencode(getVars)
    print(uri)
    # requests.get(uri)
    return uri


# throws a excception on connection failed, this should be handled externally to retry after delay
def getData(url):
    r = requests.get(url)
    print(r.status_code)

    # results should be appended in order Ward, GeoCode, value
    result = []
    if r.status_code == 200:
        # parse json
        body = r.json()["records"]
        # print(body);
        for x in body:
            ptr = x["fields"]
            if "ward_code" in ptr:
                res = (ptr["ward_name"], ptr["ward_code"], ptr["statistic"])
            else:
                res = (ptr["ward_name"], "", ptr["statistic"])
            result.append(res)
            # print(res)

            # print(x)
    return result


# url for the open Data Platform


def main():
    URL = "https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=quality-of-life-2018-19-ward&refine.indicator=%25+satisfied+with+their+local+area"
    unity = urlparse(URL)
    datasetYear = ["2017-18", "2018-19", "2019-20", "2020-21"]
    datasetTemplate = "quality-of-life-2018-19-ward"
    dataset = "quality-of-life-2018-19-ward"
    indicator = "% satisfied with their local area"
    u = buildUrl(dataset, indicator)
    r = getData(u)
    dict = {}

    for x in datasetYear:
        template = f"quality-of-life-{x}-ward"
        print(template)
        u = buildUrl(template, indicator)
        r = getData(u)
        dict[x] = r

    print(dict)

    # print (unity)
    # fetch = requests.get(URL)
    # print(fetch.status_code)
    # print(fetch.json())
    return


if __name__ == "__main__":
    sys.exit(int(main() or 0))
