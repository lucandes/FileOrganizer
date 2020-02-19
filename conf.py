import os
import nav
import exe
from time import sleep

def YorN(question):
    while True:
        inp = input(question+' (Y/N): ').upper()
        if inp == 'Y' or inp == 'N':
            break

    if inp == 'Y':
        return True
    return False

class App:
    def __init__(self):
        self.targetDir = ''

        self.dirNames = [
        'Compressed Files', 
        'Image Files', 
        'Video Files', 
        'Torrent Files', 
        'Document Files', 
        'DVD Images Files',
        'Executable Files', 
        'Programing Files']

        self.formList = [
        'zip rar whl deb', 
        'jpg jpeg png gif', 
        'mpeg mp4 mkv', 
        'torrent', 
        'txt doc pdf docx lib pdf pptx odt', 
        'iso', 
        'exe', 
        'py pyw ini msi c cpp java js']

        # turns formList's strings in lists
        for i in range(len(self.formList)):
            self.formList[i] = self.formList[i].split(' ')

        self.numOfDirs = len(self.dirNames)
        

    # start of the program
    def start(self):
        print("\nFILE ORGANIZER\nCreated by: Lucas Fernandes\n\n")
        sleep(1)

        self.browser = nav.Browser()
        print(os.getcwd())
        if YorN("Use current directory?"):
            self.targetDir = os.getcwd()
        else:
            self.targetDir = self.browser.start()

        # config selection
        while True:
            self.printConfig()
            if YorN("Use current configuration?"):
                break
            else:
                self.editConfig()

        self.fileorg = exe.FO(self)

        self.fileorg.run()

    def checkSudo(self):
        uid = os.getuid()
        if uid:
            print("Admin privileges are disabled. Errors may occur while moving files.")
            sleep(1)
            if not YorN("Proceed?"):
                return 0
        return 1

    def printConfig(self):
        print()

        for i in range(len(self.dirNames)):
            print("." * 60)
            print("%d. %s:" % (i + 1, self.dirNames[i]))

            for form in self.formList[i]:
                print("- %s" % form)
            sleep(1)
        print("." * 60)

    def editConfig(self):
        # directory number
        while True:
            num = int(input("\nEnter a directory number to edit or '0' to create a new directory: "))

            if (num < 0 or num > self.numOfDirs):
                print("Invalid directory.")
                continue

            # new directory
            if (num == 0):
                newDir = input("Enter the name of the new directory: ")
                if not newDir in self.dirNames:
                    self.dirNames.append(newDir)
                    self.formList.append([])
                    self.numOfDirs += 1
                    return 1 # quit but restart

            # edit a directory
            else:
                num -= 1

                print("\n1. Add format\n2. Remove format\n3. Remove directory")
                op = int(input("Select the operation: "))
                self.editDir(num, op)
                return 1 # quit but restart

            break

    def editDir(self, num, op):
        # add new format
        if op == 1:
            newFormat = input("\nEnter the new format: ")

            while '.' in newFormat:
                newFormat = newFormat.replace('.', '')

            if newFormat in self.formList[num]:
                print("The format already is in the current directory.")
                return

            self.formList[num].append(newFormat)

        # remove a format
        elif op == 2:
            rmvFormat = input("Enter the format: ")

            while '.' in rmvFormat:
                rmvFormat = rmvFormat.replace('.', '')

            if not rmvFormat in self.formList[num]:
                print("This format is not in the current directory.")
                return
            else:
                self.formList[num].remove(rmvFormat)

        # remove directory
        elif op == 3:
            if YorN("Are you sure you want to remove '%s'?" % self.dirNames[num]):
                self.dirNames.pop(num)
                self.formList.pop(num)
                self.numOfDirs -= 1

        else:
            print("Invalid operation number")