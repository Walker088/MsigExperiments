#!/usr/bin/env python3
import pandas as pd
import numpy as np

# ['nodeNum', 'nodeIndex', 'blocksize', 'TotalHeights', 'Throughput', 'Overhead', 'Latency']
summaryTable = pd.read_csv('./summary.csv')
header = ['blocksize', 'Throughput', 'Overhead', 'Latency']
bsTable = pd.DataFrame(columns=header)

for bsz in range(200,2200,200):
    bs_tmp = summaryTable[summaryTable['blocksize']==bsz]
    bs_tmp = bs_tmp.groupby(by='nodeNum').mean()
    bs_tmp = bs_tmp.loc[:,['blocksize', 'Throughput','Overhead','Latency']]
    bsTable = pd.concat([bsTable, bs_tmp])

bsTable.to_csv('./bszsum.csv')
