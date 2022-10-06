zork = 0
init = 0
print('List of Numbers: 9 90 31 25 41')
for thing in [9, 90, 31, 25, 41]:
    init = zork
    zork = zork + thing
    print(init, '+', thing, '=', zork)
print('Total numbers: ', zork)