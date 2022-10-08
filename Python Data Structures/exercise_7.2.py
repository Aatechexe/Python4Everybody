# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
num = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = line.find(" ")
    y = line.find(" ",x)
    z = float(line[y+1:])
    num = num + z
    count = count+1
    
print("Average spam confidence:",num/count)