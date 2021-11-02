'''
#--------------------------------------------------------
# File      : L00092017_Q4_File_1.py
# Created   : 02/11/2021 10:38
# Author    : M.Houston
# Version   : v1.0.0
# Description:  This script will cycle through a range of ports and
                return any open ports

# (c) 2021 Malcolm Houston
# Available under GNU Public License (GPL)
#-------------------------------------------------------
'''
if __name__ == '__main__':
    '''
    This is the main function
    
    This will check for open ports in a range and return whether open
    
    Parameters: host
    
    returns: port
    
'''
# Import required modules
import socket

# Define function to test for open ports
def is_port_open(host, port):
    s = socket.socket() # creates a new socket
    try:
        s.connect((host, port)) # tries to connect to host using the ports
        s.settimeout(0.1) # improve speed of scan
    except:
        return False # If cannot connect because port is closed, return False
    else:
        return True # If the connection was established, port is open! return True

host = input("Enter the host IP Address : ") # Get the host IP from the user

for port in range(21,80): # Iterate over ports, from 21 to 81
    if is_port_open(host, port):
        if port == 22: # Return SSH if Port 22 open
            print(f"SSH:{port} is open     ")
    elif port == 80: # Return HTTP if Port 80 open
            print(f"HTTP:{port} is open     ")