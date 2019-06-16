import FileOrg, navPATH, time, os

print('\nFILE ORGANIZATOR 1.0\n')
time.sleep(1)

print('Current directory:', os.getcwd())

if navPATH.YorN('Organize current directory?'):
    currentDirectory = os.getcwd()
else:
    currentDirectory = navPATH.browser()

FileOrg.runFO()

input('NOT IMPLEMENTED YET')