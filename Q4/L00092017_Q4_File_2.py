"""
#--------------------------------------------------------
# File      : L00092017_Q4_File_2.py
# Created   : 02/11/2021 10:38
# Author    : M.Houston
# Version   : v1.0.0
# Description:  This script will cycle through a range of ports and
                return any open ports

# (c) 2021 Malcolm Houston
# Available under GNU Public License (GPL)
#-------------------------------------------------------
"""
''' Sockets code to carry out a port scan '''
''' Modified from:  Network Examples 1 by Ruth Lennon, LYIT'''

import socket
import subprocess
import sys
from datetime import datetime


def port_scan():
    """
    This function will carry out a port scan on a virtual machine
    """
    # Clear the screen  #use clear if running in  *nix
    subprocess.call("cls", shell=True)

    # Ask for input
    remoteserver = input("Enter a remote host to scan: ")
    remoteserverip = socket.gethostbyname(remoteserver)
    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", remoteserverip)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()
    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)
    # We also put in some error handling for catching errors
    try:
        # try 1, 1025 if you have time
        for port in range(21, 81):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteserverip, port))
            if port == 22:  # Return SSH if Port 22 open
                print(f"SSH:{port} is open     ")
            elif port == 80:  # Return HTTP if Port 80 open
                print(f"HTTP:{port} is open     ")
            elif result == 0:
                print("Port {}:    Open".format(port))
                sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()
    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1
    # Printing the information to screen
    print('Scanning Completed in: ', total)


if __name__ == '__main__':
    '''
     This is the main function

     This will check for open ports in a range and return whether open

     Parameters: host, port range

     returns: open ports in scan
     
     '''
    port_scan()
