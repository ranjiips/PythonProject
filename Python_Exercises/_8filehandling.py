"""
File I/O
'w' - Write-Only mode
'r' - Read-Only mode
'r+' - Read and Write mode
'a' - Append mode
"""
import json
from logging import exception

import requests

listValue = [1, 2, 3]
filepath = './../files/sample.txt'
listOfThingsDo = ["You need at least to: \n", "Eat fried Ice Cream\n", "Go to Disney\n", "Travel to the moon\n", "Cook Pineapple Pizza\n", "Dance Salsa\n"]
import pandas as pd
import string
import _10genericmethods
class FileHandling(object):

    def __init__(self, path):
        self.filepath = path
        # self.filemode=mode
        self.writefile = ''
        self.readfile = ''
        self.readwritefile=open(self.filepath, 'r+')
        self.appendfilecontent=''
        self.dfobj = _10genericmethods.GenericMethods()

    def write_file_content(self, filecontent, mode):
        print('*'*20+' Write content into File '+'*'*20)
        with open(self.filepath, mode) as self.writefile:
            for content in filecontent:
                self.writefile.write(str(content) + '\n')
            print('Successfully written content into file')
        # self.writefile.close()

    def read_file_content(self, mode):
        with open(self.filepath, mode) as self.readfile:
            print('*' * 20 + ' Read content From File ' + '*' * 20)
            print(str(self.readfile.read()))
            # print(str(self.readfile.readline()))
        # self.readfile.close()

    def read_write_file_content(self,text):
        print('*' * 20 + ' Read/Write content From File ' + '*' * 20)
        # self.readwritefile = open(self.filepath, mode)
        self.readwritefile.write(str(text) + '\n')
        for lines in self.readwritefile:
            print(str(lines))
        self.readwritefile.close()

    def is_value_present_file(self, searchvalue):
        print('*' * 20 + f' Check given value \'{searchvalue}\' present in File ' + '*' * 20)
        self.readfile = open(self.filepath, 'r')
        found = 0
        for lines in self.readfile:
            if searchvalue in lines:
                found += 1
                break
        if found>0:
            print(f'Given Value is present: {searchvalue}')
        else:
            print(f'Given Value is not present: {searchvalue}')
        self.readfile.close()

    def append_content_into_file(self,content):
        print('*' * 20 + ' Append content into File ' + '*' * 20)
        self.appendfilecontent=open(self.filepath,'a')
        self.appendfilecontent.writelines(content)
        print('Successfully append content into file')
        self.appendfilecontent.close()

    def write_into_csv(self, path):
        data = {
            'ID': [20,22,22,23],
            'ItemName': ['Clock', 'Battery', 'Gas', 'Pin'],
            'ItemPrice': [400, 580, 1000, 55]
        }
        # Make data frame of above data
        df = pd.DataFrame(data)
        # append data frame to CSV file
        df.to_csv(path, mode='a', index=False, header=False)

    def get_user_details(self,filepath):
        df = self.dfobj.get_data_frame(filepath)
        url = df['API URL'].values[0]
        response = requests.get(url)
        return response.json()


# class Error(exception):
#     pass
# class NotValidFileError(Error):
#     pass


my_file = FileHandling(filepath)

# my_file.write_file_content(listValue, 'w')
# my_file.read_file_content('r')
# my_file.read_write_file_content('Ranjith')
# my_file.is_value_present_file('4')
# my_file.append_content_into_file(listOfThingsDo)
# my_file.read_file_content('r')
# my_file.is_value_present_file('Disney')

path = "C:/Ranjith/Learnings/Projects/itemdetails.csv"
# path = 'file.csv'
# df = my_file.get_data_frame(path)
# print(df.keys())
# print(df.ItemName.values)
my_file.write_into_csv(path)
# df = my_file.get_data_frame(path)
# print(df)
path = 'apifile.csv'
userdetail = my_file.get_user_details(path)
print(userdetail)
path = 'apifile1.csv'
data =  userdetail['data']
df = pd.DataFrame(data)
df.to_csv(path, index=False)
