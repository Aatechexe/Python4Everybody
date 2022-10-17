import re
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2009'
y = re.findall('\S+@\S+', x)
z = re.findall('\S+@\S+?',x)
print('Greedy', y)
print('Non Greedy', z)
