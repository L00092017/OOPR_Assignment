'''
#--------------------------------------------------------
# File      : L00092017_Q1_File_1.py
# Created   : 01/11/2021 20:31
# Author    : M.Houston
# Version   : v1.0.0
# Description:  Script to connect to local VM via SSH and verify the connection

# (c) 2021 Malcolm Houston
# Available under GNU Public License (GPL)
#-------------------------------------------------------
'''

if __name__ == '__main__':
    '''
    This is the main function
    
    This will start the SSH Connection to local VM using SSH
    
    Parameters: none
    
    returns: none
    
'''
    import paramiko

    host = "192.168.15.132"
    port = 22
    username = "l00092017"
    password = "l00092017"

    command = "ls"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

