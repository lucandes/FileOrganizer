import time, os, configFO as cf, fileOrg as fo

while True:
    cf.run()
    if not fo.run2():
        print('Restarting...')
        time.sleep(1)
        continue
    print('NOT IMPLEMENTED YET')
    break
