import os, shutil

def test():
    try:
        os.mkdir('/home/randury/Downloads/hey')
    except:
        print('Already exists hey')

    mainDir =  '/home/randury/Downloads'

    for file in os.listdir(mainDir+'/hey/'):
        if file != 'hey':
            shutil.move(mainDir+'/hey/'+file, mainDir+'/'+file)

a = '0123456789'
print(list(range(len(a))))
