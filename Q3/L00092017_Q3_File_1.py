'''
#--------------------------------------------------------
# File      : L00092017_Q3_File_1.py
# Created   : 01/11/2021 23:20
# Author    : M.Houston
# Version   : v1.0.0
# Description:  This script will parse a webpage and extract the Header text.

# (c) 2021 Malcolm Houston
# Available under GNU Public License (GPL)
#-------------------------------------------------------
'''

if __name__ == '__main__':
    '''
    This is the main function
    
    This will scrape the Apache2 Default landing page on a VM for the Headers and print them out
    
    Parameters: URL
    
    returns: Headers
    
'''
# Import required packages
import requests
from bs4 import BeautifulSoup

headers=[] # Define list variable to empty

response = requests.get("http://192.168.15.132") # Define URL to parse
soup = BeautifulSoup(response.text, "html.parser")

# Loop through each class called "section_header" and add to list removing \n
for res in soup.find_all("div",{"class":"section_header"}):
    headers.append(res.text.strip())

# print list of headers
print(headers)