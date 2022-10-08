fname = input("Enter file name: ")
fh = open(fname)
for sw in fh:
    se = sw.rstrip()
    print (se.upper())