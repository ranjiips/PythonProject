
import requests
import pandas as pd

class GenericMethods(object):

    def get_data_frame(self, file_name):
        try:
            if file_name.endswith('.csv'):
                df = pd.read_csv(file_name, dtype=str, delimiter=',')
                return df
            elif file_name.endswith('.xlsx'):
                df = pd.read_excel(file_name)
                return df
            else:
                raise Exception("please pass valid files like .csv/.xlsx")
        except FileNotFoundError as inst:
            print(inst)
        except Exception as e:
            print('Exception Occured:\n'+str(e))
