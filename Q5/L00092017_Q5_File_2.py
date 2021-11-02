'''
#--------------------------------------------------------
# File      : L00092017_Q5_File_2.py
# Created   : 02/11/2021 13:44
# Author    : M.Houston
# Version   : v1.0.0
# Description:  

# (c) 2021 Malcolm Houston
# Available under GNU Public License (GPL)
#-------------------------------------------------------
'''

if __name__ == '__main__':
    '''
    This is the main function
    
    This will do this
    
    Parameters:
    
    returns
    none
    
'''
import paramiko
import time
def ssh_connection():
global user_file
global cmd_file
	try: #selected_user_file = open(user_file, 'r')
		ip = "192.168.37.143"
		user_name="l0012345".rstrip("\n")
		user_password="l0012345".rstrip("\n")
		session = paramiko.SSHClient()

session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
		session.connect(ip.rstrip("\n"),
username=user_name, password=user_password)
		connection = session.invoke_shell()
		session.exec_command("mkdir This\n")