# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

import collections
collections.Callable = collections.abc.Callable

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
i = 0
tags = soup('a')
print(url)
for tag in tags:
    i = i + 1
    if i != 3:
        continue
    print(tag.get('href', None))

    url2 = tag.get('href', None)
    html2 = urllib.request.urlopen(url2, context=ctx).read()
    soup2 = BeautifulSoup(html2, 'html.parser')
    j = 0
    tags2 = soup2('a')
    for tag2 in tags2:
        j = j + 1
        if j != 3:
            continue
        #Page 2
        print(tag2.get('href', None))

        url3 = tag2.get('href', None)
        html3 = urllib.request.urlopen(url3, context=ctx).read()
        soup3 = BeautifulSoup(html3, 'html.parser')
        k = 0
        tags3 = soup3('a')
        for tag3 in tags3:
            k = k + 1
            if k != 3:
                continue
            #Page 3
            print(tag3.get('href', None))

            url4 = tag3.get('href', None)
            html4 = urllib.request.urlopen(url4, context=ctx).read()
            soup4 = BeautifulSoup(html4, 'html.parser')
            l = 0
            tags4 = soup4('a')
            for tag4 in tags4:
                l = l + 1
                if l != 3:
                    continue
                #Page 4
                print(tag4.get('href', None))
            
    