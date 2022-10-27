import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1647993.xml (Sum ends with 74)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
# print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
count = 0
sum = 0
for item in results:
    count = count + 1
    sum = sum + int(item.find('count').text)

print('Count: ', count)
print('Sum: ', sum)

