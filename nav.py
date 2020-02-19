import os
from time import sleep

def YorN(question):
    while True:
        inp = input(question+' (Y/N): ').upper()
        if inp == 'Y' or inp == 'N':
            break

    if inp == 'Y':
        return True
    return False

class Browser:
	def __init__(self):
		self.target = '/'
		self.listdir = []
		self.selected = False

	def start(self):
		while not self.selected:
			self.listdir = os.listdir(self.target)

			# filtering directories
			for file in self.listdir:
				filepath = os.path.join(self.target, file)

				if not os.path.isdir(filepath):
					self.listdir.remove(file)

			# printing directories
			print('-' * 50)
			for item in self.listdir:
				print('-', item)
				sleep(0.05)
			print('-' * 50)

			# recieving user input
			print("Enter the directory name, '..' to return or press Enter to select the current directory.")
			print(self.target, end='') if self.target == '/' else print(self.target, end="/")
			usr = input()

			if len(usr) == 0:
				if YorN("Select current directory?"):
					self.selected = True

			elif usr == '..':
				if self.target == '/':
					print("\nYou are already in the root directory.")
					sleep(1)
					continue
				self.target = self.target.split('/')
				self.target.pop(-1)
				self.target = '/'.join(self.target)
				if self.target == '': self.target = '/' 

			elif os.path.isdir(os.path.join(self.target, usr)):
				self.target = os.path.join(self.target, usr)

			else:
				print("\nThe selected directory is invalid. Try again.")
				sleep(1)
				continue

		return self.target