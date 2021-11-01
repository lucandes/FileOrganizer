import conf

<<<<<<< HEAD
assert ('linux' in sys.platform), 'This program runs on Linux only'
while True:
    cf.run()

    fo.run2()
    if not cf.YorN('\n'+str(fo.filesFound)+' files with matching formats found. Proceed?'):
        print('Restarting...')
        time.sleep(1)
        continue
    
    fo.runFinal()
    break
=======
def main():
    app = conf.App()
    if not app.checkSudo():
        return

    app.start()


main()
>>>>>>> 27398bc0533806e0b791822b5204dc1239ed0945
