file =  input("Enter the file name:")
if len(file) < 1:
    file = "clown.txt"

doku = dict()
data = open(file)
for word in data:
    word = word.rstrip()
    #print(word)

    words = word.split()
    #print(words)
    i = 0
    j = len(words)
    for strg in words:
        #print ("**strg: **", strg)
        doku[strg] = doku.get(strg,0) + 1
        i = i + 1
        #print ("Interation: ",i,"Of",j,doku)
print(doku)
bigvalue = None
bigkey = None
for k,v in doku.items():
    #print(k,v)
    if bigvalue is None or v > bigvalue:
        bigvalue = v
        bigkey = k
print()
print("The Biggest Word : ", bigkey,bigvalue)
