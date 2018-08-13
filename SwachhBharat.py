# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:57:42 2018

@author: Siddharth
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def SwachhataStatus():
    
    fileName = "./data/NumberOfVillages.xlsx"
    sheet = "Sheet1"
    dfs = pd.read_excel(fileName, sheet_name=sheet)
#    print(dfs)

    records = [json.loads (line) for line in open ('./data/Swachha.json')]
    columns = [col['label'] for col in records[0]['fields']]
    data = records[0]['data']
    df = pd.DataFrame(data, columns = columns)
    gb = df.groupby('StateName').size().to_frame(name='Count').reset_index()
    
    gb = gb.merge(dfs, on='StateName')
    gb['Percent'] = (gb.Count/gb.TotalVillages)*100
    print (gb)


    

    fig, ax = plt.subplots()
    fig.set_size_inches(20,10)
    
    plt.barh(gb['StateName'], gb['Percent'], tick_label = gb['StateName'], 
        color=(0.2, 0.4, 0.2, 0.6))
    ax.set_ylabel("States")
    ax.set_xlabel("Percentages")
    ax.set_title("Swachha Bharat")
    ax.xaxis.set_major_formatter(ticker.PercentFormatter())
    
    
    # create a counter to iterate over list
    i = 0


    # set individual bar lables using above list
    for bar in ax.patches:
    # get_width pulls left or right; get_y pushes up or down
        ax.text(bar.get_width() + .3, bar.get_y()+0.38, str(int(gb.Count[i])), 
                fontsize=10, fontweight = 'bold', color='red')
        i += 1
# invert for largest on top 
    ax.invert_yaxis()

    
    plt.show()
#    gb.plot(kind='barh', y=gb['Percent'], title ='Swachha Bharat Abhiyaan', figsize=(15, 10), legend=True, fontsize=12)
    
#print ([rec[2] for rec in records[0]['data']])

SwachhataStatus()