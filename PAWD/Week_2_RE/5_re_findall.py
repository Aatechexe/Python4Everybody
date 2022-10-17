import re
x = 'My favorite numbers are 19 and 42'
y = re.findall('[AIUEO]+', x)
print(y)