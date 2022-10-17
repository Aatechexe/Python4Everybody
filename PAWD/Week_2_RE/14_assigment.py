from functools import total_ordering
import re
sum = 0
hand = open('regex_sum_1647989.txt')
all = list()
for line in hand:
    line = line.rstrip()
    #print (line)
    # if re.findall('[0-9]+',line):
    #     print(line)
    #     print(re.findall('[0-9]+',line))

    stuff = re.findall('[0-9]+',line)
    if len(stuff) <= 0:
        continue
    #print(stuff,len(stuff))
   
    for number in stuff:
        #print ("Sebelum: ", sum)
        number = int(number)
        sum = sum + number
        #print("Setelah :", sum)
print("Sum: ", sum)
