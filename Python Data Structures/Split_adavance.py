data = open('mbox-short.txt')
for line in data:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    if not len(words)>2:
        continue
    print(words[2])