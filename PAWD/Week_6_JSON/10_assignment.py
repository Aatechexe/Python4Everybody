import urllib.request, urllib.parse, urllib.error
import json
import ssl

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1647994.json (Sum ends with 20)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

# parms = dict()
# url = urllib.parse.urlencode(address)

uh = urllib.request.urlopen(address, context=ctx)
data = uh.read().decode()

info = json.loads(data)
print('User count:', len(info))
data = info["comments"]

count = 0
sum = 0
for item in data:
    count = count + 1
    sum = sum + int(item['count'])

print('Count: ', count)
print('Sum: ', sum)
