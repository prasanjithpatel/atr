import os
import pandas as pd


read = "/home/prasanjith/Desktop/atr/silver/FOREXCOM_XAGUSD_3m.csv"
read1 = "/home/prasanjith/Desktop/atr/silver/FOREXCOM_XAGUSD_ytd.csv"

read2 = pd.read_csv(read)
read3 =pd.read_csv(read1)

read2.to_json("silver_3m", orient='records')
read3.to_json("siver60",orient="records")