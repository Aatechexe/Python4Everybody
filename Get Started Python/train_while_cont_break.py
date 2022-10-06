while True:
    line = input('Enter name of tim: ')
    #jika dua huruf pertama dimulai FC
    #line[0] = huruf awal 
    #line[:1] satu huruf pertama
    if line[:2] == 'FC' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')