#-*- coding: utf-8 -*-
import os, time, configFO as cf, shutil as st


################################
def getKey(file_format):
    for flist in range(len(cf.default.formindex)):
        if file_format in cf.default.formindex[flist]:
            return flist+1
    return False

def createDir(mainDirectory):
    direIndex = 0
    dirCount = 0

    for dire in filesToMoves:
        if len(dire) != 0:
            dirName = cf.default.formname[ direIndex ]
            try:
                os.mkdir( mainDirectory +'/'+ dirName )
                dirCount += 1
            except FileExistsError:
                print('- The directory', dirName,'already exists.')
        direIndex += 1
    return dirCount

def moveFiles(mainDirectory):
    direIndex = 0
    fileCount = 0

    for direct in filesToMoves:
        dirName = cf.default.formname[ direIndex ]
        for file in filesToMoves[direIndex]:
            try:
                st.move(mainDirectory+'/'+file, mainDirectory+'/'+dirName+'/'+file)
                fileCount += 1
            except FileNotFoundError:
                #print('The file "{}" could not be moved'.format(file))
                pass
        direIndex += 1
    return fileCount

def run2():
    global filesFound
    filesFound = 0

    for file in os.listdir(cf.currentDirectory):
        if '.' in file:
            temp = file.split('.')[-1]
            
            if temp in ' '.join(cf.default.formats.values()):
                if getKey(temp):
                    filesToMoves[getKey(temp)-1].append(file)
                    #print('"{}" added to filesToMove[{}]'.format(file, getKey(temp)))
                    filesFound += 1
    return filesFound

def runFinal():
    try:
        print('\nCreating directories...')
        print(createDir(cf.currentDirectory), 'directories created\n')
        
        filesMoved = moveFiles(cf.currentDirectory)
        print('\nFiles moved: {}/{}'.format(filesMoved, filesFound))
        

        input('PRESS ENTER TO QUIT')
        
    except:
        print('AN ERROR OCURRED')

###############################################################

filesToMoves =[]
for list in cf.default.formindex:
    filesToMoves.append([])
