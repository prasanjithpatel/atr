import os
import pandas as pd


read = "/home/prasanjith/Desktop/atr/Bulk-Deals-09-08-2023-to-09-08-2024.csv"
#read1 = "/home/prasanjith/Desktop/atr/silver/FOREXCOM_XAGUSD_ytd.csv"

read2 = pd.read_csv(read)
#read3 =pd.read_csv(read1)

read2.to_json("Bulk_deals.json", orient='records')
#read3.to_json("one_day.json",orient="records")