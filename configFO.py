#-*- coding: utf-8 -*-
import os, time, navPATH

#####################################

def removeDot(format):
    if '.' in format:
        format = format.replace('.','')
    return format

def checkDuplicate(format):
    allFormats = [default.formindex[0], default.formindex[1], default.formindex[2], default.formindex[3], default.formindex[4], default.formindex[5]]
    for flist in allFormats:
        for form in flist:
            allFormats.append(form)
            #print('AQ Ó: ',flist, allFormats)
            try:    
                allFormats.remove(flist)
            except ValueError:
                continue
    if format in flist:
        return False
    else:
        return True

def checkDir(directoryIndex):
    if str(directoryIndex) in '123456':
        return True
    else:
        return False

def YorN(question):
        if input(question+' (Y/N): ').upper() == 'N':
            return False
        else:
            return True 

def selfprint(group, formats):
    print('='*30)
    print(group)
    formats = formats.split(' ')
    for i in formats:
        print(i) if i[0] == '.' else print('.'+i)
        time.sleep(0.1)

def checkAndTest(format):
    format = removeDot(format)

    if YorN('Add '+format+' to directory "'+self.formname[categoryNum]+'"?'):
        self.formdict[categoryNum].append(format)
   
    else:
        print('\nOperation Cancelled')
        time.sleep(1)
        return False

def currentDir():
    print('Current directory:', os.getcwd())
    if navPATH.YorN('Organize current directory?'):
        #print('DONWLOADS WINDOWS SELECIONADO')
        #return '/media/randury/Reservado pelo Sistema/Users/Debslu/Downloads'
        return os.getcwd()
    else:
        return navPATH.browser()

def run():
    print('---------------------')
    print('\nFILE ORGANIZATOR 1.0\n')
    time.sleep(1)

    global currentDirectory
    currentDirectory = currentDir()

    print('\nCONFIGURATION\n')
    time.sleep(1)
    confSelected = False

    while not confSelected:
        selfprint('1- Compressed Files:', default.formindex[0])
        selfprint('2- Image Files:', default.formindex[1])
        selfprint('3- Video Files:', default.formindex[2])
        selfprint('4- Torrent Files:', default.formindex[3])
        selfprint('5- Document Files:', default.formindex[4])
        selfprint('6- CD/DVD Files:', default.formindex[5])
        print('='*30)

        if not YorN('\nUse this configuration?'):
            opSelect = input('\nEnter "add" or "remove" to select the operation: ')

            if opSelect == 'add':
                dirIndex = int(input('Enter the directory index to be edited: '))-1
                if not checkDir(dirIndex):
                    print('Directory Error: invalid directory')
                    time.sleep(1)
                    continue
                formatToEdit = input('Enter the format: ')

                if checkDuplicate(formatToEdit):
                    default.addFormats(dirIndex, formatToEdit)
                    if YorN('Edit another format?'):
                        continue
                    break
                else:
                    print('Format error: the inputed format is already in a directory')
                    time.sleep(1)
                    continue
            if opSelect == 'remove':
                dirIndex = int(input('Enter the directory index to be edited: '))-1
                if not checkDir(dirIndex):
                    print('Directory Error: invalid directory')
                    time.sleep(1)
                    continue
                formatToEdit = input('Enter the format: ')

                if checkDuplicate(formatToEdit):
                    default.rmvFormats(dirIndex, formatToEdit)
                    if YorN('Edit another format?'):
                        continue
                    break
                else:
                    print('Format error: the inputed format is already in a directory')
                    time.sleep(1)
                    continue
            else:
                print('\nOperation Error: invalid operation')
                time.sleep(2)
                continue
        confSelected = True
            
#####################################
class Config:
    def __init__(self):
        self.formats = {
        'fzip':'zip rar', 
        'fimg':'jpg jpeg png gif', 
        'fvid':'mpeg mp4 mkv', 
        'ftor':'torrent', 
        'fdoc':'doc pdf docx lib pdf pptx', 
        'fiso':'iso'}
        
        self.formindex = [
        self.formats['fzip'], 
        self.formats['fimg'], 
        self.formats['fvid'], 
        self.formats['ftor'], 
        self.formats['fdoc'], 
        self.formats['fiso']
        ]

        self.formname = [
        'Compressed Files', 
        'Image Files', 
        'Video Files', 
        'Torrent Files', 
        'Document Files', 
        'CD/DVD Files']
     
    def addFormats(self, directoryNum, newformat):
        if YorN('\nEnter {} format to directory "{}"?: '.format(newformat, default.formname[directoryNum])):
            self.formindex[directoryNum] = self.formindex[directoryNum]+' '+newformat
            print('Operation was successful')
        else:
            print('\nOperation cancelled')
    
    def rmvFormats(self, directoryNum, newformat):
        # REFAZ ESSA MERDA AQUI MALUCO
        if YorN('\nRemove {} format from directory "{}"?:'.format(newformat, self.formname[directoryNum])):
            try:
                self.formindex[directoryNum] = self.formindex[directoryNum].split(' ')
                self.formindex[directoryNum].pop(-1)
                self.formindex[directoryNum] = ' '.join(self.formindex[directoryNum])
                print('NEW FORMAT LIST:', self.formindex[directoryNum])
                print('Operation was successful')
            except ValueError:
                print('Format error: directory {} has no format {}'.format(self.formname[directoryNum], newformat))
        else:
            print('\nOperation cancelled')
#####################################

default = Config()