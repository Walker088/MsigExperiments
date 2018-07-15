#!/usr/bin/env python3
import pandas as pd
import numpy as np

# ['nodeNum', 'nodeIndex', 'blocksize', 'dura', 'TotalHeights', 'Throughput', 'Overhead', 'Latency']
summaryTable = pd.read_csv('./summary.csv')
header = ['dura', 'Throughput', 'Overhead', 'Latency']
duraLst = [5, 10, 25, 35, 50]
bsTable = pd.DataFrame(columns=header)

for dura in duraLst:
    bs_tmp = summaryTable[summaryTable['dura']==dura]
    bs_tmp = bs_tmp.groupby(by='nodeNum').mean()
    bs_tmp = bs_tmp.loc[:,['dura', 'Throughput','Overhead','Latency']]
    bsTable = pd.concat([bsTable, bs_tmp])

bsTable.to_csv('./bszsum.csv')
