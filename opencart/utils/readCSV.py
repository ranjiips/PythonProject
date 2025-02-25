import pandas as pd
import logging
import os

# dir_path = os.path.dirname(os.path.realpath(__file__))

class ReadCSV(object):

    def read_data_from_csv(self):
        csvPath = ".\\opencart\\resources\\registration.csv"
        # logging.info(f"CSV file path: {csvPath}")
        # logging.info(f"Current directory path: {dir_path}")
        # logging.info(f"Current working directory path: {os.getcwd()}")

        self.data = pd.read_csv(csvPath).T.to_dict()
        return self.data

    # print(data)

    # If you want to fetch specific fields from each dictionary entry
    # for key, value in data.items():
    #     print(f"Key: {key}")
    #     print(f"FirstName: {value['FirstName']}")
    #     print(f"LastName: {value['LastName']}")
    #     print(f"Email: {value['Email']}")
    #     print(f"Password: {value['Password']}")
    #     print("------")