fname = input("Enter file name: ")
fh = open(fname)
lst = list()
i = 0
for line in fh:
    text = line.split()
    for i in text:
        if not i in lst:
            lst.append(i)
lst.sort()
print(lst)
    