sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

if fh <= 40:
    print("Regular")
    pay = fh * fr
else:
    print("Overtime")
    rp = 40*fr
    op = (fh - 40)*fr * 1.5
    pay = rp + op
print("Pay:",pay)