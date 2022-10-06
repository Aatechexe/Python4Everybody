#Function for compute pay
def computepay(hours, rate):
    print("In computepay ",hours, rate)
    if hours > 40:
        #print("Overtime")
        rp = 40*rate
        op = (hours - 40)*rate * 1.5
        pay = rp + op
    
    else:
        #print("Regular")
        pay = hours * rate
        
    #print("Returning", pay)
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

p = computepay(fh, fr)
print("Pay", p)