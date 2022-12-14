# -*- coding: utf-8 -*-
"""whitney.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w1LK5ersQivltSToVgA___8G93p6r6D1
"""

import requests
from bs4 import BeautifulSoup
import urllib

url = "https://whitney.org/collection/works?page=1&q%5Bclassification_cont%5D=Paintings&q%5Bhas_image_true%5D=1"
response = requests.get(url)
whitney_soup = BeautifulSoup(response.text, 'html.parser')
print(whitney_soup.title)

def whitney_paintings():
    whitneyPaintings = []

    for i in range(1,77):
        url = "https://whitney.org/collection/works?page="+str(i)+"&q%5Bclassification_cont%5D=Paintings&q%5Bhas_image_true%5D=1"
        response = requests.get(url)
        whitney_soup = BeautifulSoup(response.text, 'html.parser')
        print("page" + str(i))
        for item in whitney_soup.find_all('img'):
            iurl = item['src']
            whitneyPaintings.append(iurl)
            urllib.request.urlretrieve(iurl, "allWhitneyPaintings/"+iurl.split('/')[-1])

            
    print(whitneyPaintings[0:10])
    print(len(whitneyPaintings))

def whitney_prints():
    whitneyPrints = []

    for i in range(1,260):
        url = "https://whitney.org/collection/works?page="+str(i)+"&q%5Bclassification_cont%5D=Prints&q%5Bhas_image_true%5D=1"
        response = requests.get(url)
        whitney_soup = BeautifulSoup(response.text, 'html.parser')
        print("page" + str(i))
        for item in whitney_soup.find_all('img'):
            iurl = item['src']
            whitneyPrints.append(iurl)
            urllib.request.urlretrieve(iurl, "allWhitneyPrints/"+iurl.split('/')[-1])

            
    print(whitneyPrints[0:10])
    print(len(whitneyPrints))

whitney_prints()