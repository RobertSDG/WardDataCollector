"""Class to build a dataset from multiple sources & disaggregations"""
import sys

import WardDataCollector
import DeprivationDataCollector

class DataCollector(object):
    """description of class"""
    def __init__(self,indicator):
        self.indicator = indicator

    def get_data (self)->dict:
        results = {}
        results['Ward'] = WardDataCollector.dataset_builder(self.indicator)
        deprivation = DeprivationDataCollector(self.indicator)
        results['Deprivation'] = deprivation.dataset_builder(self.indicator)

        return results




def main():
    """entry point for quickly checking function"""
    indicator = "% households which have experienced severe food insecurity"
    d = DataCollector(indicator)
    i = d.get_data()
    print(i)
    return 0

if __name__ == "__main__":
    sys.exit(int(main() or 0))
