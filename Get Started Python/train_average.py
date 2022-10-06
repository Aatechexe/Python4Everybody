count = 0
sum = 0
print('Value: 9, 10, 14, 15, 21, 45, 25')
for value in [9, 10, 14, 15, 21, 45, 25]:
    count = count + 1
    sum = sum + value
    print(count, sum)
print('Mean = ', sum, "/",count,"=", sum/count)