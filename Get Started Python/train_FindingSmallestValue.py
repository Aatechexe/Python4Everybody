smallest = None
print('Before', smallest)
print('Value: 9 41 12 3 74 15 60')
for value in [9, 41, 12, 3, 74, 15, 60]:
    if smallest is None :
        smallest = value
    elif value < smallest:
        smallest = value
    print('smallest so far: ', smallest, 'Recent number: ', value)
print('After: ', smallest)