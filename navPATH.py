import os, time, sys

#####################################

def printFiles(directory):
    if len(os.listdir(directory)) > 0:
        for arquivo in range(len(os.listdir(directory))):
            print(str(arquivo+1)+'.', os.listdir(directory)[arquivo])
            time.sleep(0.1)
    else:
        print('-EMPTY DIRECTORY-')

def dirIsValid(directory):
    try:
        os.listdir(directory)
        return True
    except FileNotFoundError:
        return False

def YorN(question):
    if input(question+' (Y/N): ').upper() == 'N':
        return False
    else:
        return True 

def browser():
    currentDirectory = '/'
    pathHistory = ['/']
    fileSelected = False
    directoryIsValid = False

    time.sleep(1)
    while not fileSelected:
        print('='*30)
        printFiles(currentDirectory)
        while not directoryIsValid:
            print('='*30)
            print('Type a directory name, ".." to return, or press enter to select the current directory')
            inputDirectory = input(currentDirectory)
            

            # input to return
            if inputDirectory == '..':
                if not len(pathHistory) > 1:
                    print('\nInvalid Directory Input: the current directory is not a subdirectory')
                    time.sleep(1)
                    break
                pathHistory.pop(-1)
                currentDirectory = pathHistory[-1]
                break
            # input to proceed with the program
            elif inputDirectory == '':
                if YorN('\nOrganize directory "'+currentDirectory+'"?'):
                    fileSelected = True
                    break
            # input is a directory
            else:
                if dirIsValid(currentDirectory+inputDirectory):
                    currentDirectory = currentDirectory+inputDirectory+'/'
                    pathHistory.append(currentDirectory)
                    break
                else:
                    print('\nInvalid Directory Input: directory not found')
                    time.sleep(1)
                    continue 

    return currentDirectory
    
#####################################
