"""Class to pull deprivation data from the API"""
import sys
from urllib.parse import urlencode

import requests

class DeprivationDataCollector(object):
    """Class to access time series of deprivation data from bristol open data api"""

    __datasets = {
        "2017-18":"qol-deprivation-dataset-2017_18-v2",
        "2018-19":"quality-of-life-2018-19-deprivation",
        "2019-20":"quality-of-life-2019-20-deprivation",
        "2020-21":"quality-of-life-2020-21-deprivation"
        }

    def build_url(self, dataset:str, refine_indicator:str):
        """ builds the url to access a dataset """
        get_vars = {"dataset": dataset, "rows": 50, "refine.indicator": refine_indicator}
        base_url = "https://opendata.bristol.gov.uk/api/records/1.0/search/?"
        uri = base_url + urlencode(get_vars)
        print(uri)
        # requests.get(uri) 
        return uri

    def get_data(self, url:str):
        response = requests.get(url)
        print(response.status_code)

        # results should be appended in order Ward, GeoCode, value
        result = []
        if response.status_code == 200:
            # parse json
            body = response.json()["records"]
        # print(body);
            for row in body:
                ptr = row["fields"]
                # 'deprivation_decile': ['Least Deprived 10%','.Most Deprived 10%']

                if "ward_code" in ptr:
                    res = [ptr["ward_name"], ptr["ward_code"], ptr["statistic"]]
                else:
                    res = ["", "", ptr["statistic"]]
                result.append(res)
                # print(res)

                # print(x)
        return result

    def dataset_builder(self, indicator: str) -> dict:
        """Returns dictionary containing results for the indicator by year"""
        result_set = {}
        for key in self.__datasets:
            print(self.__datasets[key])
            url = self.build_url(self.__datasets[key], indicator)
            response = self.get_data(url)
            result_set[key] = response
        return result_set

    

def main():
    """entry point for quick dirty testing"""
    deprivation_data_collector = DeprivationDataCollector()
    print (deprivation_data_collector.dataset_builder("% households which have experienced moderate to severe food insecurity"))
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))