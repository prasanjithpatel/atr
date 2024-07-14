import json
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np


Forex = ["AUDCAD", "AUDUSD", "EURJPY", "GBPJPY", "GBPUSD", "USDJPY","Gold","silver"]


save_path = '/home/prasanjith/Desktop/atr/Results/result.png'

for coin in Forex:
    File_path = '/home/prasanjith/Desktop/atr/'+str(coin)+'/result.json'
    save_path = '/home/prasanjith/Desktop/atr/Results/'+str(coin)+'.png'

    with open(File_path, 'r') as file:
        data = json.load(file)

    strategy = data[0]['strategy']
    Trade_days_profit = defaultdict(list)
    Trade_days_max_profit = defaultdict(list)

    graph = 'nonProfitDays'
    graph1 = 'profitDays'
    strategy = data[0]['strategy']
    Trade_days_profit = defaultdict(list)
    Trade_days_max_profit = defaultdict(list)

    #graph = 'nonProf

    num_pd = len(data[0][graph1])
    num_npd = len(data[0][graph])

    for i in range(num_pd):
        Trade_days_profit[data[0][graph1][i]['entryIndex']].append(data[0][graph1][i]['profit'])
        Trade_days_max_profit[data[0][graph1][i]['entryIndex']].append(data[0][graph1][i]['maxProfit'])

    for i in range(num_npd):
        Trade_days_profit[data[0][graph][i]['entryIndex']].append(data[0][graph][i]['profit'])
        Trade_days_max_profit[data[0][graph][i]['entryIndex']].append(data[0][graph][i]['maxProfit'])

    profit  = {k: sum(v) for k, v in Trade_days_profit.items()}
    max_profit = {k: sum(v) for k, v in Trade_days_max_profit.items()}

    # Extract keys and their corresponding sums
    keys = list(profit.keys())
    keys = sorted(keys)
    #print(keys)


    profit_values = list(profit.values())
    max_profit_values = list(max_profit.values())
    # Define the width of the bars
    bar_width = 0.4

    # Create an array of positions for the x-axis
    r1 = np.arange(len(keys))
    r2 = [x + bar_width for x in r1]

    # Create the bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(r1, profit_values, color='blue', width=bar_width, edgecolor='grey', label='Profit')
    plt.bar(r2, max_profit_values, color='red', width=bar_width, edgecolor='grey', label='Max Profit')

    # Add labels and title
    plt.xlabel('Entry Index', fontweight='bold')
    plt.ylabel('Profit', fontweight='bold')
    plt.title(str(coin)+" "+str(strategy), fontweight='bold')
    plt.xticks([r + bar_width / 2 for r in range(len(keys))], keys)

    # Add legend
    plt.legend()
    plt.grid(True)



    plt.savefig(save_path, format='png')
    # Show the plot
    plt.show()