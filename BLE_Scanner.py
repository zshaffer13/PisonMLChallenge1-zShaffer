# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:39:07 2021

@author: zshaf
"""

import asyncio
from bleak import BleakScanner, discover, BleakClient
import time

devices_dict = {}
devices_list = []
receive_data = []
details_list = []

async def scan():
    dev = await discover()
    for i in range(0,len(dev)):
        #print("[" + str(i) + "]" + dev[i].address,dev[i].name,dev[i].metadata["uuids"])
        #Put devices information into list
        devices_dict[dev[i].address] = []
        devices_dict[dev[i].address].append(dev[i].name)
        devices_dict[dev[i].address].append(dev[i].metadata["uuids"])
        devices_list.append(dev[i].address)
        details_list.append(dev[i].metadata["uuids"])
# =============================================================================
#     async with BleakScanner() as scanner:
#         await asyncio.sleep(5.0)
#     for d in scanner.discovered_devices:
#         print(d)
# =============================================================================
    #print(devices_list)
    details_list_remv = [i for i in details_list if i ]
    print(details_list_remv)
    textfile = open("metadata_file.txt",'w')
    for element in details_list_remv:
        textfile.write(str(element) +'\n')
    textfile.close

asyncio.run(scan())
