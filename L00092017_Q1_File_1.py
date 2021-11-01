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
import paramiko

def start_connection():
    u_name = 'l00092017'
    pswd = 'l00092017'
    port = 22
    r_ip = '198.162.15.131'

    myconn = paramiko.SSHClient()
    myconn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    session = myconn.connect(r_ip, username=u_name, password=pswd, port=port)

    remote_cmd = 'ifconfig'
    (stdin, stdout, stderr) = myconn.exec_command(remote_cmd)
    print("{}".format(stdout.read()))
    print("{}".format(type(myconn)))
    print("Options available to deal with the connectios are many like\n{}".format(dir(myconn)))
    myconn.close()

if __name__ == '__main__':
    '''
    This is the main function
    
    This will connect to local VM using SSH
    
    Parameters: username, password
    
    returns: none
    
'''
    start_connection()
