#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import json
import json
import datetime
import re
import time
import subprocess as sp


def findAllWallet(path):
    """
    搜索所有的待分析的文本文件，将文件名存放列表中返回
    """
    list = []
    for root,dirs,files in os.walk(path):
        for file in files:
            filePath = os.path.join(root,file)
            if "README.md" in filePath:
                continue
            list.append(filePath)
    return list

def getBalanceFromWallet(wallet_list):
    sum=0
    for wallet in wallet_list:
        address=sp.getoutput(f"helium-wallet -f {wallet} info" + " |grep '| Address' | awk '{print $4}'")
        balance=float(sp.getoutput(f"helium-wallet -f {wallet} info" + " |grep '| Balance' | awk '{print $4}'"))
        sum+=balance
        print(f"{address} {balance}")
    return sum



if __name__ == '__main__':
    wallet_list=findAllWallet("/Users/liudeshan/Documents/work/wallet")
    print(f"Sum: {getBalanceFromWallet(wallet_list)}")