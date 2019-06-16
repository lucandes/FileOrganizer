#-*- coding: utf-8 -*-
import os, time

#####################################

def removeDot(format):
    if '.' in format:
        format = format.replace('.','')
    return format

def checkDuplicate(format):
    allFormats = [default.fzip, default.fimg, default.fvid, default.ftor, default.fdoc, default.fiso]
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
    if directoryIndex in '123456':
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

def runFO():
    print('\nCONFIGURATION\n')
    time.sleep(2)
    confSelected = False

    while not confSelected:
        selfprint('1- Compressed Files:', default.fzip)
        selfprint('2- Image Files:', default.fimg)
        selfprint('3- Video Files:', default.fvid)
        selfprint('4- Torrent Files:', default.ftor)
        selfprint('5- Document Files:', default.fdoc)
        selfprint('6- CD/DVD Files:', default.fiso)
        print('='*30)

        if not YorN('\nUse default configuration?'):
            opSelect = input('\nEnter "add" or "remove" to select the operation: ')

            if opSelect == 'add':
                dirIndex = input('Enter the directory index to be edited: ')
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
                dirIndex = input('Enter the directory index to be edited: ')
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
        self.fzip = ['zip', 'rar']
        self.fimg = ['jpg', 'jpeg', 'png', 'gif']
        self.fvid = ['mpeg', 'mp4', 'mkv']
        self.ftor = ['torrent']
        self.fdoc = ['doc', 'pdf', 'docx', 'lib', 'pdf', 'pptx']
        self.fiso = ['iso']
        self.formdict = {'1':self.fzip, '2':self.fimg, '3':self.fvid, '4':self.ftor, '5':self.fdoc, '6':self.fiso}
        self.formname = {'1':'Compressed Files', '2':'Image Files', '3':'Video Files', '4':'Torrent Files', '5':'Document Files', '6':'CD/DVD Files'}

    def addFormats(self, directoryNum, newformat):
        if YorN('\nEnter {} format to directory "{}"?: '.format(newformat, default.formname[directoryNum])):
            self.formdict[directoryNum].append(newformat)
            print('Operation was successful')
        else:
            print('\nOperation cancelled')
    
    def rmvFormats(self, directoryNum, newformat):
        # REFAZ ESSA MERDA AQUI MALUCO
        if YorN('\nRemove {} format from directory "{}"?:'.format(newformat, directoryNum)):
            try:
                self.formdict[directoryNum].remove(newformat)
                print('Operation was successful')
            except ValueError:
                print('Format error: directory {} has no format {}'.format(self.formname[directoryNum], newformat))
        else:
            print('\nOperation cancelled')
#####################################

default = Config()