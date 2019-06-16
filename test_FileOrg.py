print('-'*40, '\nSELECT FORMATS', '\n'+'-'*40)
print('Default formats:\n')



while True:

    selfprint('1- Compressed Files:', fzip)
    selfprint('2- Image Files:', fimg)
    selfprint('3- Video Files:', fvid)
    selfprint('4- Torrent Files:', ftor)
    selfprint('5- Document Files:', fdoc)
    selfprint('6- CD/DVD Files:', fiso)
    
    print('\nTo add a new format use: add .format num\nTo remove a format use:  rmv .format\nPress Enter to continue\n')
    while True:
        customFormat = input('> ')
        if len(customFormat) >= 6 and customFormat[:3] == 'add':
            if customFormat[4] == '.':
                try:
                    customFormat = customFormat.split(' ')
                    formdict[customFormat[2]].append(customFormat[1])
                    print('Operation Sucessful!')
                    print('UPDATING LIST')
                    time.sleep(1)
                    break
                except KeyError:
                    print(customFormat[3], 'is not a list index')
                    continue
            else:
                print('Invalid format: ex.: "add .rar"')
                continue

        elif len(customFormat) >= 6 and customFormat[:3] == 'rmv':
            if customFormat[4] == '.':
                try:
                    customFormat = customFormat.split(' ')
                    formdict[customFormat[2]].remove(customFormat[1][1:])
                    print('Operation Sucessful!')
                    print('UPDATING LIST')
                    time.sleep(1)
                    break
                except ValueError:
                    print(customFormat[1], 'format is not on the list', customFormat[2])
                    continue

            else:
                print('Invalid format: ex.: "rmv .rar"')
                continue
        
        if customFormat == '':
            break

        else:
            print('INVALID INPUT\n')
            continue
    

#makeDIR() # criar pastas
a = 'jsaid'