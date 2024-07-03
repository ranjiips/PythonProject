"""
File I/O
'w' - Write-Only mode
'r' - Read-Only mode
'r+' - Read and Write mode
'a' - Append mode
"""
import json
import os.path
from logging import exception
from robot.libraries.BuiltIn import BuiltIn

import requests
import pandas as pd
import _10genericmethods
base_url="https://rahulshettyacademy.com"
get_book_id="/Library/GetBook.php"
addbookurl = "/Library/Addbook.php"
deletebookurl = "/Library/DeleteBook.php"
bookId = "ADBH04567"
class ExploreAPI(object):

    def __init__(self):
        self.get_df = _10genericmethods.GenericMethods()

    def get_request_api(self, apiURL):
        try:
            response =  requests.get(apiURL)
            if response.status_code!=200:
                raise Exception(f"GET request failed with the status code: {response.status_code}")
            else:
                return response
        except Exception:
            raise Exception()

    def post_request_api(self, apiURL, payload):
        try:
            response = requests.post(apiURL,json=payload)
            if response.status_code!=200:
                raise Exception(f"POST request failed with the status code: {response.status_code}")
            else:
                return response
        except Exception as e:
            print('Exception Occured: ' + str(e))

    def get_all_user_details(self,filepath):
        df = self.get_df.get_data_frame(filepath)
        url = df['API URL'].values[0]
        response = requests.get(url)
        return response.json()

    def get_user_details_by_id(self,filepath, id):
        df = self.get_df.get_data_frame(filepath)

        df.set_index("API_Type", inplace=True)
        result = df.loc["GET_USER_BY_ID"]
        print(result)
        # url = df['API URL'].values[1]
        # response = requests.get(f'{url}{id}')
        url = f'{result[0]}{id}'
        response = requests.get(url)
        return response.json()

    def add_book_json_payload(self):
        filepath = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.dirname(filepath)+r'\files\addBook.json'
        with(open(filepath, 'r')) as f:
            fileContent = f.read()
            fileContent = fileContent.replace('Book_Name','CSharp')
            fileContent = fileContent.replace('Book_isbn','ADBH')
            fileContent = fileContent.replace('Book_aisle','04567')
            fileContent = fileContent.replace('Book_author','Ranjith')
        #payload = json.dumps(fileContent)
        payload = str(fileContent)
        print(payload)
        apiURL = f'{base_url}{addbookurl}'
        response = self.post_request_api(apiURL, payload)
        print(f"Response content: {response.text}")


myobj = ExploreAPI()
url = f"{base_url}{get_book_id}?ID={bookId}"
response = myobj.get_request_api(url)
print(response.text)
myobj.add_book_json_payload()




