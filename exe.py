import os
import shutil

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
		self.numOfDirs = conf.numOfDirs
		self.toMove = []
		for i in range(self.numOfDirs):
			self.toMove.append([])
		self.found = 0
		self.moved = 0
		self.created = 0

	def run(self):
		# searching for compatible files
		self.search(self.target, self.formats)

		if not YorN(str(self.found)+" files found. Proceed?"):
			return

		# creating the necessary directories
		self.createDirs(self.target, self.dirs)

		print(self.created, " new directories have been created.")
		print("Moving files...")

		# moving files
		self.move(self.target, self.dirs)

		print("Files moved: "+str(self.moved)+"/"+str(self.found))



	def search(self, target, formats):
		dirList = os.listdir(target)

		for item in dirList:
			format = item.split('.')[-1]

			for i in range(self.numOfDirs):
				if format in formats[i]:
					self.toMove[i].append(item)
					self.found += 1
					break

	def createDirs(self, target, dirNames):
		for i in range(self.numOfDirs):
			if len(self.toMove[i]) > 0:
				try:
					path = os.path.join(target, dirNames[i])
					os.mkdir(path)
					self.created += 1
				except FileExistsError:
					continue

	def move(self, target, dirNames):
		for i in range(self.numOfDirs):
			dirpath = os.path.join(target, dirNames[i])

			for file in self.toMove[i]:
				filepath = os.path.join(target, file)
				
				# moving file
				shutil.move(filepath, dirpath)

				# checking if it was succesful
				if file in os.listdir(dirpath):
					self.moved += 1


