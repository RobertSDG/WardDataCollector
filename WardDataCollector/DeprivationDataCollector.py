"""Class to pull deprivation data from the API"""
import sys


class DeprivationDataCollector(object):
    """Class to access time series of deprivation data from bristol open data api"""

    __datasets = {
        "2017-18":"qol-deprivation-dataset-2017_18-v2",
        "2018-19":"quality-of-life-2018-19-deprivation",
        "2019-20":"quality-of-life-2019-20-deprivation",
        "2020-21":"quality-of-life-2020-21-deprivation"
        }

    def build_url(dataset, refine_indicator):
        get_vars = {"dataset": dataset, "rows": 50, "refine.indicator": refine_indicator}
        base_url = "https://opendata.bristol.gov.uk/api/records/1.0/search/?"
        uri = base_url + urlencode(get_vars)
        print(uri)
        # requests.get(uri)
        return uri

def main():
    deprivation_data_collector = DeprivationDataCollector()
    print (deprivation_data_collector.build_url("foo", "bar"))
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))