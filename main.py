import os
import paramiko
import subprocess
import time
import logging
from datetime import datetime
import sys


def sshCommand(hostname, port, username, password, command):
    sshClient = paramiko.SSHClient()                                   # create SSHClient instance
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())    # AutoAddPolicy automatically adding the hostname and new host key
    #host = sshClient.get_host_keys()
    #host.clear()
    #print(sshClient.load_system_host_keys())  
    sshClient.connect(hostname, port, username, password)
    stdin, stdout, stderr = sshClient.exec_command(command)
    result = stdout.readlines()
    #result = ''.join(stdout.readlines())
    #print(result)
    return  result[-1].strip()


    
    for elem in data:
        flag=False
        try:
            if elem[3]=='Linux' and elem[0][0]!='#':
                #print("enter")
                flag=True
                value = sshCommand(elem[0],22,elem[1],elem[2],'ofed_uninstall.sh --force')
                print(value)
                compare = value.rstrip("\n")
                #print("Asd")
                if compare=='Uninstall finished successfully':
                    #print("asad")
                    return elem[0]+' : ofed uninstallation was successful'
                else:
                    #print("asad")
                    return  elem[0]+' : ofed uninstallation was unsuccessful'
        except:
            if flag==True and elem[0][0]!='#':
                return elem[0]+' : ofed already been uninstalled'
                #print("H")
    
    
    
dictionary = dict()
file = open('reference.txt')
for each in file:
    if each != '\n':
        dictionary[each.split()[0]] = each.split()[1]
#print(dictionary)


iso_list = os.listdir(os.getcwd())
#print(iso_list)

for elem in dictionary.keys()::
        flag=False
        try:
            if dictionary[elem][0]!='#':
                #print("enter")
                flag=True
                value = sshCommand(dictionary[elem],22,'root','Hptc_ib','ofed_uninstall.sh --force')
                print(value)
                compare = value.rstrip("\n")
                #print("Asd")
                if compare=='Uninstall finished successfully':
                    #print("asad")
                    return dictionary[elem]+' : ofed uninstallation was successful'
                else:
                    #print("asad")
                    return  dictionary[elem]+' : ofed uninstallation was unsuccessful'
        except:
            if flag==True and dictionary[elem][0]!='#':
                return dictionary[elem]+' : ofed already been uninstalled'
'''for item in iso_list:
    for each in dictionary.keys():
        
        if each in item and 'alternate-aarch64' not in item:
            print(item+" was copied to "+dictionary[each])
            os.system('cmd /c "pscp -r -pw Hptc_ib "'+item+'" root@"'+dictionary[each]+'":/root/"')
        if 'MLNX_OFED Documentation Rev 5.1-2.5.8.0__12_02_2020' in item:
            os.system('cmd /c "pscp -r -pw Hptc_ib "'+item+'" root@"'+dictionary[each]+'":/root/"')'''
    