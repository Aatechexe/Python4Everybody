largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        num = float(num)
    except :
        print('Invalid input')
        continue
    
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
        
    if num == "done":
        break

print("Maximum is", largest)
print("Minimum is", smallest)