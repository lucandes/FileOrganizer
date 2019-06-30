import time, os, configFO as cf, fileOrg as fo, sys

assert ('linux' in sys.platform), 'This program runs on Linux only'
while True:
    cf.run()

    fo.run2()
    if not cf.YorN('\n'+str(fo.filesFound)+' files with matching formats founded. Proceed?'):
        print('Restarting...')
        time.sleep(1)
        continue
    
    fo.runFinal()
    break
