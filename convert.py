import pandas as pd

one_day_data = pd.read_csv("FOREXCOM_XAUUSD, 2.csv")
hour_data_data = pd.read_csv("/home/prasanjith/Desktop/atr/FOREXCOM_XAUUSD, D.csv")
one_day_data.to_json('fox1.json', orient='records')
hour_data_data.to_json('fox2.json',orient = 'records')