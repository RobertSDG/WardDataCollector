"""Class to build a dataset from multiple sources & disaggregations"""
import sys
import csv

import WardDataCollector
from DeprivationDataCollector import DeprivationDataCollector


class DataCollector(object):
    """description of class"""

    def __init__(self, indicator):
        self.indicator = indicator

    def get_data(self) -> dict:
        results = {}
        results["Ward"] = WardDataCollector.dataset_builder(self.indicator)
        deprivation = DeprivationDataCollector()
        results["Deprivation"] = deprivation.dataset_builder(self.indicator)
        self.retrieved_dataset = results
        return results

    def data_to_csv(self):
        with open(self.indicator + "-universal.csv", mode="w") as employee_file:
            data_writer = csv.writer(
                employee_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            data_writer.writerow(
                ["Year", "Series", "Deprivation decile", "Ward", "GeoCode", "Value"]
            )
            for year in self.retrieved_dataset["Ward"]:
                for i in self.retrieved_dataset["Ward"][year]:
                    row = [year, "Ward", "", i[0], i[1], i[2]]
                    data_writer.writerow(row)

            for year in self.retrieved_dataset["Deprivation"]:
                for i in self.retrieved_dataset["Deprivation"][year]:
                    row = [year, "Deprivation", i[0], "", "", i[1]]
                    data_writer.writerow(row)

        return


def main():
    """entry point for quickly checking function"""
    indicator = "% who agree they can influence decisions that affect their local area"
    d = DataCollector(indicator)
    i = d.get_data()
    d.data_to_csv()
    print(i)
    return 0


if __name__ == "__main__":
    sys.exit(int(main() or 0))
