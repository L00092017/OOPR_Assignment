"""
#--------------------------------------------------------
# File      : L00092017_Q3_File_2.py
# Created   : 01/11/2021 23:20
# Author    : M.Houston
# Version   : v1.0.0
# Description:  This script will parse a webpage and extract the text from
                any section_header class and export result to csv file.

# (c) 2021 Malcolm Houston
# Available under GNU Public License (GPL)
#-------------------------------------------------------
"""

if __name__ == '__main__':
    '''
    This is the main function
    
    This will scrape the Apache2 Default landing page on a VM for the headers text,
    print out and export to a csv file.
    
    Parameters: URL
    
    returns: headers
    
'''
# Import required packages
import csv
import requests
from bs4 import BeautifulSoup


# Define headers list variable to empty
headers = []


# Define URL to parse
response = requests.get("http://192.168.15.132")
soup = BeautifulSoup(response.text, "html.parser")

# Loop through each class called "section_header" and add to list removing \n
for res in soup.find_all("div", {"class": "section_header"}):
    headers.append(res.text.strip())

# Search URL for all occurances of the word Apache2
pattern = "Apache2"
words = soup.find(text=lambda text: text and pattern in text)
word_count = len(words)

# print list of headers and word count
print(headers)
print("The total number of occurances of " + pattern + " is: "+ str(word_count))


# Export list of headers to a CSV file
with open('header_list.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(headers)
