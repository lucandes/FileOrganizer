#-*- coding: utf-8 -*-
import os
import time

def navpath():
    initDir = '/'
    pathlist = []
    print('\nStarting navigation mode:')
    time.sleep(1)

    while True: # repita o processo de acesso a pasta imprimindo seu conteúdo
        print('-'*30)
        
        if len(os.listdir(initDir)) < 50:
            for i in range(len(os.listdir(initDir))):         # para cada arquivo na pasta atual
                print(str(i+1)+'.', os.listdir(initDir)[i])   # escreva o arquivo
                time.sleep(0.1)                             # espere 0.1 segundo
        else:
            for i in range(len(os.listdir(initDir))):         # para cada arquivo na pasta atual
                print(str(i+1)+'.', os.listdir(initDir)[i]) 

        while True: # repita a pergunta caso o diretório digitado seja inválido
            print('\nType a directory name, ".." to return, or press enter to select the current directory')
            temp = input(initDir[1:]+'/')
            if temp == '..':
                break
            elif temp != '':
                try:                             # cheque se o diretório é válido
                    os.listdir(initDir+'/'+temp)
                    break
                except FileNotFoundError:        # caso o diretório seja invalido, repita
                    print('Error: Directory not found')
                    continue
            else:
                break

        
        if temp != '':
            if temp == '..':
                if len(pathlist) > 1:
                    initDir = pathlist[-1]
                    pathlist.pop(-1)
                    continue
                else:
                    print('Error: the current directory does not have a parent directory')
            else:
                pathlist.append(initDir)  # /                   # pathlist = ['/', '//home']
                initDir = initDir+'/'+temp  # //home
                print('\nOpening directory /'+temp+':')
                continue
        else:
            print('*'*30)
            print('\nDirectory selected: '+initDir[1:])

            return initDir


#--------------------------------
print('\nFILE ORGANIZATOR 1.0')
#--------------------------------
while True:
    print('-'*40)
    print('\nCurrent directory:', os.getcwd())
    time.sleep(1)
    if input('Organize current directory? (Y/N): ').upper() == 'N': 
        mydir = navpath()
        mydir = mydir[1:]
    else:
        mydir = os.getcwd()

    print('\nDirectory content:')
    for i in range(len(os.listdir(mydir))):
        print('-', os.listdir(mydir)[i])
    
    time.sleep(1)
    if input('\nProceed to organization? (Y/N): ').upper() == 'N':
        continue
    else:
        break
    