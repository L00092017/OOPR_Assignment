"""
#--------------------------------------------------------
# File      : L00092017_Q5_File_2.py
# Created   : 02/11/2021 13:44
# Author    : M.Houston
# Version   : v1.0.0
# Description:  This will create a folder structure on VM and install curl

# (c) 2021 Malcolm Houston
# Available under GNU Public License (GPL)
#-------------------------------------------------------
"""

# Import required modules
import paramiko
import sys


# Define function for ssh connection and run commands
def ssh_connection():
    """

    This function will connect to VM via SSH and run some commands

    """
    try:
        ip = "192.168.15.132"
        user_name = "l00092017".rstrip("\n")
        user_password = "l00092017".rstrip("\n")

        # Create the SSH connection to the VM
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(ip, username=user_name, password=user_password)

        # Commands to create the folder structure
        ssh.exec_command("mkdir Labs\n")
        ssh.exec_command("mkdir Labs/lab1\n")
        ssh.exec_command("mkdir Labs/lab2\n")

        # Output the directory listing to show folders created
        com = "ls ./Labs\n"  # Command variable
        stdin, stdout, stderr = ssh.exec_command(com)  # Run command
        output = ''  # Set output variable to empty
        for line in stdout.readlines():  # Populate with results of the command
            output += line
        if output:
            print("Folders structure created:\n" + output)  # Print the out directory structure
        else:
            print("There was no output for this command")  # Error check if command returns nothing

        # Command to find file last access time
        stdin, stdout, stderr = ssh.exec_command("ls -l --time=atime\n")
        output = ''  # Set output variable to empty
        for line in stdout.readlines():  # Populate with results of the command
            output += line
        if output:
            print("Apt update:\n" + output)  # Print the out directory structure
        else:
            print("There was no output for this command")  # Error check if command returns nothing

        # Commands to update app repositories
        stdin, stdout, stderr = ssh.exec_command("echo l00092017 | sudo -S apt-get update\n")
        output = ''  # Set output variable to empty
        for line in stdout.readlines():  # Populate with results of the command
            output += line
        if output:
            print("Apt update:\n" + output)  # Print the out directory structure
        else:
            print("There was no output for this command")  # Error check if command returns nothing

        stdin, stdout, stderr = ssh.exec_command("echo l00092017 | sudo -S apt-get install -y curl\n")
        output = ''
        for line in stdout.readlines():
            output += line
        if output:
            print("Curl Installed:\n" + output)
        else:
            print("There was no output for this command")  # Error check if command returns nothing

    except paramiko.AuthenticationException:
        print("Authentication Error")
        sys.exit(1)


# Run the function
if __name__ == '__main__':
    """
	This is the main function

	This will call the ssh_connection function to set a folder structure and install curl on remote VM

	Parameters: none

	returns: none
	
    """
    ssh_connection()
