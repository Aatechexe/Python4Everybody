name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short.txt"

counts = dict()
handle = open(name)
for line in handle:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    words = line.split()
    data = words[1]
    counts[data] = counts.get(data, 0) + 1


bigcount = None
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)