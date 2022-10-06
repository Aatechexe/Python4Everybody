largest = None
print('Before', largest)
print('9, 41, 12, 3, 74, 15, 60')
for value in [9, 41, 12, 3, 74, 15, 60]:
    if largest is None:
        largest = value
    elif value > largest:
        largest = value
    print('Larges so far: ', largest, 'Recent number: ', value)
print('After: ', largest)