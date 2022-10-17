import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2009'
y = re.findall('From .*@([^ ]*)', x)
print(y)