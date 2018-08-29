#!/usr/bin/env python3

import shutil
import os

def main():
    for dirPath, dirNames, fileNames in os.walk('./'):
        for file in fileNames:
            filePath = os.path.join(dirPath, file)
            #print(filePath)
            statInfo = os.stat(filePath)
            if statInfo.st_size != 0:
                #print(filePath)
                src = filePath
                subPathLst = filePath.split('/')
                #print(subPathLst)
                subPathLst = subPathLst[2:]
                if len(subPathLst) > 2:
                    subDir = './merge/'+str(subPathLst[0])
                    if not os.path.exists(subDir):
                        #print(subDir)
                        os.mkdir(subDir)
                        os.mkdir(subDir+'/logs/')
                subPath = '/'.join(subPathLst)
                dst = os.path.join('./merge/', str(subPath))
                #print(dst)
                try:
                    shutil.copy(src, dst)
                except shutil.SameFileError:
                    print('SameFileError, src: {0}, dst: {1}'.format(src, dst))
                except IsADirectoryError:
                    print('IsADirectoryError, src: {0}, dst: {1}'.format(src, dst))
                except FileNotFoundError:
                    print('FileNotFoundError, src: {0}, dst: {1}'.format(src, dst))

main()
