import os
#import paramiko
import subprocess
import time
import logging
from datetime import datetime
import sys


#os.system('cmd /c "pscp -r -pw Hptc_ib C:/Users/Administrator/Desktop/New_Automation/Firmwares root@192.168.2.128:/root/" > nul')
dictionary = dict()
file = open('reference.txt')
for each in file:
    if each != '\n':
        dictionary[each.split()[0]] = each.split()[1]
#print(dictionary)
string = "pscp -r -pw Hptc_ib 'D:\IB_Repo\Toby\OS DVDs\RHEL-8.3.0-20201009.2-x86_64-dvd1.iso' root@192.168.1.151:/root/"

iso_list = os.listdir(os.getcwd())
#print(iso_list)
os.system('cmd /k "pscp -r -pw Hptc_ib "'+"'D:\IB_Repo\Toby\OS DVDs\RHEL-8.3.0-20201009.2-x86_64-dvd1.iso\'"+'" root@192.168.1.151:/root/"')
'''for item in iso_list:
    for each in dictionary.keys():

        if each in item and 'alternate-aarch64' not in item:
            print(item+" was copied to "+dictionary[each])
            os.system('cmd /c "pscp -r -pw Hptc_ib "'+item+'" root@"'+dictionary[each]+'":/root/"')
        if 'MLNX_OFED Documentation Rev 5.1-2.5.8.0__12_02_2020' in item:
            os.system('cmd /c "pscp -r -pw Hptc_ib "'+item+'" root@"'+dictionary[each]+'":/root/"')'''
    