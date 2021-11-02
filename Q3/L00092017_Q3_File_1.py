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
# Import packages
import requests
from bs4 import BeautifulSoup

# Define URL to parse
URL = "http://192.168.15.132"
page = requests.get(URL)
# Run parser on the URL
soup = BeautifulSoup(page.content, 'html.parser')

# Loop through the URL and extract any Div class that contains the text "header"
for EachPart in soup.select('div[class*="header"]'):
    print(EachPart.get_text()) # Print out the header text
