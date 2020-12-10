import os
import paramiko
import subprocess
import time
import logging
from datetime import datetime
import sys
import re

def sshCommand(hostname, port, username, password, command):
    sshClient = paramiko.SSHClient()                                   # create SSHClient instance
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())    # AutoAddPolicy automatically adding the hostname and new host key
    #host = sshClient.get_host_keys()
    #host.clear()
    #print(sshClient.load_system_host_keys())  
    sshClient.connect(hostname, port, username, password)
    stdin, stdout, stderr = sshClient.exec_command(command)
    result = ''.join(stdout.readlines())
    #print(result)
    
    return result
    


    
  
    
    
dictionary = dict()
file = open('reference.txt')
for each in file:
    if each != '\n' and each[0]!='#':
        dictionary[each.split()[0]] = each.split()[1]
print(dictionary)


iso_list = os.listdir(os.getcwd())
#print(iso_list)
def uninstall_ofed():
    string = ''
    for elem in dictionary.keys():
        flag=False
        try:
            flag=True
            value = sshCommand(dictionary[elem],22,'root','Hptc_ib','ofed_uninstall.sh --force')
            #print(value)
            compare = value.strip('\n').split('\n')[-1]
            print(compare)
            if compare=='Uninstall finished successfully':
                string += dictionary[elem]+' : ofed uninstallation was successful\n'
            elif 'command not found' in compare:
                string += dictionary[elem]+' : ofed already been uninstalled\n'
            elif compare == '':
                string += dictionary[elem]+' : ofed already been uninstalled\n'
            else:
                string += dictionary[elem]+' : ofed uninstallation was unsuccessful\n'
        except:
            if flag==True and elem[0]!='#':
                string += dictionary[elem]+' : ofed already been uninstalled\n'
    return string

print(uninstall_ofed())

def iso_copy():
    string = ''
    for each in dictionary.keys():
        for item in iso_list:
        
            if each in item and 'alternate-aarch64' not in item:
                command = 'mkdir '+item.strip('.iso')
                sshCommand(dictionary[each],22,'root','Hptc_ib',command)
                os.system('cmd /c "pscp -r -pw Hptc_ib "'+item+'" root@"'+dictionary[each]+'":/root/"'+item.strip('.iso')+'"/" > nul')
                string += item+" was copied to "+dictionary[each]+'\n'
            
                os.system('cmd /c "pscp -r -pw Hptc_ib \"NVIDIA® MLNX_OFED Documentation Rev 5.1-2.5.8.0__12_02_2020.pdf\" root@"'+dictionary[each]+'":/root/"'+item.strip('.iso')+'"/" > nul')
                string += "NVIDIA® MLNX_OFED Documentation Rev 5.1-2.5.8.0__12_02_2020 was copied to "+dictionary[each]+'\n'

    return string

print(iso_copy())
    

def iso_mount():
    for each in dictionary.keys():
        for item in iso_list:
            if each in item:
                sshCommand(dictionary[each],22,'root','Hptc_ib','umount /mnt')
                sshCommand(dictionary[each],22,'root','Hptc_ib','mount /root/'+item.strip('.iso')+'/'+item+' /mnt')
                sshCommand(dictionary[each],22,'root','Hptc_ib','ls /mnt')
                store_data = sshCommand(dictionary[each],22,'root','Hptc_ib','cd /mnt; ./mlnxofedinstall --force')
                ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
                write_data = ansi_escape.sub('', store_data)
                print(write_data)
                with open(item.strip('.iso')+'.txt','w') as f:
                    f.write(write_data)
                sshCommand(dictionary[each],22,'root','Hptc_ib','cd /root; tar -czvf '+item.strip('.iso')+'.tar.gz '+item.strip('.iso'))
                os.system('cmd /c "pscp -r -pw Hptc_ib root@"'+dictionary[each]+'":/root/"'+item.strip('.iso')+'".tar.gz ." > nul')
               

iso_mount()