"""
#--------------------------------------------------------
# File      : L00092017_Q1_File_1.py
# Created   : 01/11/2021 20:31
# Author    : M.Houston
# Version   : v1.0.0
# Description:  Script to connect to local VM via SSH and verify the connection

# (c) 2021 Malcolm Houston
# Available under GNU Public License (GPL)
#-------------------------------------------------------
"""
import sys

if __name__ == '__main__':
    '''
    This is the main function
    
    This will start the SSH Connection to local VM using SSH
    
    Parameters: none
    
    returns: none
    
'''
    # Import required modules
    import paramiko

    # Define function for ssh connection and run commands
    def ssh_connection():

        try:  # attempt connection to VM
            # Define variables for use in the connection
            ip = "192.168.15.132"
            user_name = "l00092017".rstrip("\n")
            user_password = "l00092017".rstrip("\n")
            # Create the SSH connection to the VM
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            ssh.connect(ip, username=user_name, password=user_password)
            print("Connected to: ", ip)  # Output connected status

        # Exception error if SSH fails authentication
        except paramiko.BadAuthenticationType as e:
            print(e)
            sys.exit(1)

ssh_connection()
