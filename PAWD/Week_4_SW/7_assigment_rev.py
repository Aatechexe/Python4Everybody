from ctypes.wintypes import tagSIZE
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

import collections
collections.Callable = collections.abc.Callable

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Mae.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: D

url = input('Enter Link: ') 
count = input('Enter Count: ')
position = input('Enter Position: ')
print(url)
for i in range(int(count)):
    # print(i)
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    j = 0
    for tag in tags:
        j = j + 1
        if j != int(position):
            continue
        print(tag.get('href', None))
        url = tag.get('href', None)
