import re
hand = open('mbox-short.txt')

#1
# for line in hand:
#     line = line.rstrip()
#     if re.search('^X.*:', line):
#         print(line)

#2
# for line in hand:
#     line = line.rstrip()
#     if re.search('X-.*:', line):
#         print(line)

#3
for line in hand:
    line = line.rstrip()
    if re.search('X-.\S+:', line):
        print(line)