sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()
    
if fh > 40:
    print("Overtime")
    rp = 40*fr
    op = (fh - 40) * fr * 1.5
    pay = rp + op
else:
    print("Regular")
    pay = fh * fr
print("Pay:",pay)