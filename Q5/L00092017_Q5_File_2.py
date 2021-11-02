'''
#--------------------------------------------------------
# File      : L00092017_Q5_File_2.py
# Created   : 02/11/2021 13:44
# Author    : M.Houston
# Version   : v1.0.0
# Description:  This will create a folder structure on VM and install curl

# (c) 2021 Malcolm Houston
# Available under GNU Public License (GPL)
#-------------------------------------------------------
'''

if __name__ == '__main__':
	'''
	This is the main function
	
	This will set a folder structure and install curl on remote VM
	
	Parameters: ip, user, password
	
	returns: none
	
'''
import paramiko

def ssh_connection():
    global user_file
    global cmd_file

    try:  # selected_user_file = open(user_file, 'r')
        ip = "192.168.15.132"
        user_name="l00092017".rstrip("\n")
        user_password="l00092017".rstrip("\n")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(ip, username=user_name, password=user_password)
        print("Connected to: ", ip)
        ssh.exec_command("mkdir Labs\n")
        ssh.exec_command("mkdir Labs/lab1\n")
        ssh.exec_command("mkdir Labs/lab2\n")
        com = "ls ./Labs\n"
        stdin, stdout, stderr = ssh.exec_command(com)
        output = ''
        for line in stdout.readlines():
            output += line
        if output:
            print("Folders structure created:\n" + output)
        else:
            print("There was no output for this command")

        stdin, stdout, stderr = ssh.exec_command("echo l00092017 | sudo -S apt-get update\n")
        output = ''
        for line in stdout.readlines():
            output += line
        if output:
            print("Apt update:\n" + output)

        stdin, stdout, stderr = ssh.exec_command("echo l00092017 | sudo -S apt-get install -y curl\n")
        output = ''
        for line in stdout.readlines():
            output += line
        if output:
            print("Curl Installed:\n" + output)

    except paramiko.BadAuthenticationType as e:
        print(e)
        sys.exit(1)

ssh_connection()