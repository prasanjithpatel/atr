import pandas as pd 
import numpy as np


def date_parser(date_string):
    return pd.to_datetime(date_string, format='%m/%d/%Y %H:%M')

one_day_data = pd.read_csv(r"/home/prasanjith/Desktop/atr/XAUUSD_historical_data_one_day.csv",)
hour_data = pd.read_csv(r'/home/prasanjith/Desktop/atr/XAUUSD_historical_data.csv')

#one_day_data.to_json('one_data.json', orient='records')
#hour_data.to_json('hour_data.json',orient = 'records')
'''try:
            print(on.iloc[row_index])
        except IndexError:
            print(f"Row index {row_index} is out of bounds")
            
            1-23
            23-46
            '''

class Get_data():
    def __init__(self,one_day_data,hour_data):
        self.one_day_data = one_day_data
        self.hour_data = hour_data 
    def get_pairs(self):
        return hour_data.iloc[23:46]
    



data  = Get_data(one_day_data,hour_data)
print(data.get_pairs())
