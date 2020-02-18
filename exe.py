import os

def YorN(question):
    while True:
        inp = input(question+' (Y/N): ').upper()
        if inp == 'Y' or inp == 'N':
            break

    if inp == 'Y':
        return True
    return False

class FO:
	def __init__(self, conf):
		self.target = conf.targetDir
		self.dirs = conf.dirNames
		self.formats = conf.formList 
		self.toMove = []
		for i in range(len(self.formats)):
			self.toMove.append([])
		self.found = 0

	def run(self):
		# searching for compatible files
		self.search(self.target, self.formats)

		if not YorN(str(self.found)+" files found. Proceed?"):
			return

		# creating the necessary directories
		self.createDirs(self.target, self.dirs)

	def search(self, target, formats):
		dirList = os.listdir(target)

		for item in dirList:
			format = item.split('.')[-1]

			for i in range(len(formats)):
				if format in formats[i]:
					self.toMove[i].append(item)
					self.found += 1
					break



	def createDirs(self, target, dirNames):
		for i in range(len(self.toMove)):
			if len(self.toMove[i]) > 0:
				try:
					path = os.path.join(target, dirNames[i])
					os.mkdir(path)
				except FileExistsError:
					continue