import conf

def main():
    app = conf.App()
    if not app.checkSudo():
        return

    app.start()


main()