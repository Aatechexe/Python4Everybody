import re
hand =  open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    # if re.findall('^X-DSPAM-Confidence: ([0-9])',line):
    #     print(re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line))
    if len(stuff) !=1 : 
        continue
    #print(stuff)
    num = float(stuff[0])
    numlist.append(num)
print('Maximum: ', max(numlist))