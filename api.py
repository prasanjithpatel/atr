import requests
import json 

#url = "https://marketdata.tradermade.com/api/v1/timeseries?currency=XAUUSD&api_key=GpyZeqsYbd_Td7mIYmtZ&start_date=2024-03-1 00:00&end_date=2024-03-31 00:00&format=records&interval=hourly"

url = "https://marketdata.tradermade.com/api/v1/timeseries?currency=XAUUSD&api_key=GpyZeqsYbd_Td7mIYmtZ&start_date=2024-03-01&end_date=2024-06-30&format=records"
response = requests.get(url)



if response.status_code == 200:
    data = response.json()
    with open('forex1.json', 'w') as f:
        json.dump(data, f, indent=4)
    #
    # print(json.dumps(data, indent=4))  # pretty-print the JSON data
else:
    print("Failed to retrieve data:", response.status_code)



print(response.status_code)  # prints the HTTP status code
#print(response.content)  # prints the response content