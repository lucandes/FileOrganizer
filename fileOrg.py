#-*- coding: utf-8 -*-
import os, time, configFO as cf


################################
def getKey(file_format):
    for flist in range(len(cf.default.formindex)):
        if file_format in cf.default.formindex[flist]:
            return flist
    return False

def run2():
    filesToMove = {
        'fzip':[], 
        'fimg':[], 
        'fvid':[], 
        'ftor':[], 
        'fdoc':[], 
        'fiso':[]}
    
    filesToMoveIndex = [
        filesToMove['fzip'], 
        filesToMove['fimg'], 
        filesToMove['fvid'], 
        filesToMove['ftor'], 
        filesToMove['fdoc'], 
        filesToMove['fzip'], 
    ]

    fcounter = 0
    for file in os.listdir(cf.currentDirectory):
        if '.' in file:
            temp = file.split('.')[-1]
            
            if temp in ' '.join(cf.default.formats.values()):
                if getKey(temp):
                    filesToMoveIndex[getKey(temp)].append(file)
                    #print('"{}" added to filesToMove[{}]'.format(file, getKey(temp)))
                    fcounter += 1
    return cf.YorN('\n'+str(fcounter)+' files with matching formats founded. Proceed?')

