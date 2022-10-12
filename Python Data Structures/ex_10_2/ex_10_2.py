name =  input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

data = dict()
for line in handle:
    line = line.rstrip()
    #print(line)
    if not line.startswith("From"):
        #print("Line not start From")
        continue
    #print("Yes Line Start From")
    #print(len(line))
    words = line.split()
    if len(words) < 3:
        continue
    words = words[5].split(":")
    #print(words)
    words = words[0]
    data[words] = data.get(words,0) + 1
    #print(data)
    #print(words, len(words))
#print(data)
lst = list()
for k,v in data.items():
    newsetup = (k,v)
    lst.append(newsetup)

lst.sort()
for k,v in lst:
    print(k, v)

