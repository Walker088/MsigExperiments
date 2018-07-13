#!/usr/bin/env python3
import pandas as pd
import numpy as np
import os

def makeTable(header, rawConTimePath, rawStartConPath, fileName):
    try:
        rawConTime = pd.read_csv(rawConTimePath, header=None)
        rawStartCon = pd.read_csv(rawStartConPath, header=None)
    except:
        print("rawConTimePath", rawConTimePath, "rawStartConPath", rawStartConPath)
    arr = np.zeros([rawConTime.shape[0],len(header)])
    for i in range(1, rawConTime.shape[0]+1):
        try:
            arr[i-1][0] = i #Height
            arr[i-1][1] = rawConTime.loc[i-1,1]/(10**6)  #ConTime
            arr[i-1][2] = rawConTime.loc[i-1,3] #Txs
            arr[i-1][3] = (rawStartCon.loc[i,1]-rawStartCon.loc[i-1,1])/(10**6) #TotalTime 
            arr[i-1][4] = arr[i-1][3]-arr[i-1][1] #NonConTime
        except KeyError as k:
            print(k, "index:", i)
            continue
    arr[0][5] = (rawConTime[3].sum())/(rawStartCon.loc[rawStartCon.shape[0]-1,1]-rawStartCon.loc[0,1])*(10**9) #throughput
    res_df = pd.DataFrame(arr,columns=header)
    res_df.to_csv(fileName)

def runCalcu(header):
    for nodeNum in range(4,8,4):
        for blocksize in range(1200,1400,200):
            for nodeIndex in range(1,nodeNum+1):
                rawConTimePath = ("./{1}-{0}node/ConsensusTimeNode{2}-{1}-{0}node.csv".format(nodeNum, blocksize, nodeIndex))
                rawStartConPath = ("./{1}-{0}node/StartConNode{2}-{1}-{0}node.csv".format(nodeNum, blocksize, nodeIndex))
                pathName = ("./{1}-{0}node/node{2}.csv".format(nodeNum, blocksize, nodeIndex))
                makeTable(header, rawConTimePath, rawStartConPath, pathName)

def main():
    header = ["Height","ConTime","Txs","TotalTime","NonConTime","Throughput"]
    runCalcu(header)

main()
#########################################

