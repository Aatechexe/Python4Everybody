import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2009'
# Parentheses are not part of the match - but they tell
# where to start and stop what string to extract
y = re.findall('^From (\S+@\S+)', x)

print('Greedy', y)

