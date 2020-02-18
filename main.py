import conf

def main():
    app = conf.App()
    app.checkSudo()

    app.start()


main()