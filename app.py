from sys import platform
import os  #path, getcwd, listdir
import sys #exit, argv
import shutil #move

class App:
	def __init__(self):
		self.system_linux = self.get_system() #still don't know what to do with this XD
		self.conf_file = self.find_conf_file()
		self.conf_dict = {}
		self.found_files = {}
		self.misc_files = []
		self.move_misc = False

		# counters
		self.found_files_counter = 0
		self.misc_files_counter = 0
		self.created_folders_counter = 0
		self.moved_files_counter = 0
		self.failed_files_counter = 0

		#parameters
		self.yes_to_all = False
		self.quiet = False

	def run(self):
		if (len(sys.argv) == 1):
			self.print_usage()
			sys.exit()

		self.get_parameters()
		
		if not os.path.isdir(self.target_dir_path):
			sys.exit("Error: invalid dir '%s'"%(self.target_dir_path))

		if not self.conf_file:
			sys.exit("Error: no configuration file.")

		self.conf_dict = self.get_dict_from_file()
		self.found_files = self.scan_target_dir()
		
		self.create_directories()

		if not self.yes_to_all and not self.quiet:
			print("Organizer is about to move", self.found_files_counter, "files. Continue? (Y/N): ", end="")
			if input().lower() != 'y':
				sys.exit("Error: process stopped by user.")

		self.move_files()

		if not self.yes_to_all and not self.quiet:
			print("\nThere are", self.misc_files_counter ,"files that have no directory.")
			print("Move to a new 'Misc' folder? (Y/N): ", end="")
			if input().lower() != 'y':
				self.move_misc = False
			else:
				self.move_misc = True

		if self.move_misc:
			self.misc()


		if not self.quiet:
			self.show_results()

	def get_parameters(self):
		for param in sys.argv:
			# program name
			if param == sys.argv[0]:
				continue

			# read parameters
			if param[0] == '-' and len(param) > 1:
				for char in param[1:]:
					if char == 'y':
						self.yes_to_all = True
						continue
					if char == 'q':
						self.quiet = True
						continue
					sys.exit("Error: invalid parameters.")

			# check if is dir
			elif os.path.isdir(param):
				self.target_dir_path = param
				continue

			else:
				self.print_usage()
				sys.exit()
		
	def get_system(self):
		if "linux" in platform:
			return True
		return False

	def find_conf_file(self):
		files = os.listdir(os.getcwd())
		if "config.txt" in files:
			config_path = os.path.join(os.getcwd(), "config.txt")
			return config_path
		return False

	def print_usage(self):
		print("USAGE: python", sys.argv[0], "<target_dir_path> (-qy)")
		print("Parameters:")
		print("-y : Ignore questions")
		print("-q : No output")
		print()

	def get_dict_from_file(self):
		config = open(self.conf_file, 'r')
		lines = config.read().split("\n")

		temp_dict = {}			# will be returned
		current_dir = ''		# to set the directories
		current_formats = []	# to group formats from the directory
		has_dir = False			# check if any dir was read
		has_formats = False		# check if any format was read
		loop_counter = 0		# counts lines from loop

		for line in lines:
			loop_counter += 1

			# empty line
			if len(line) == 0:
				continue

			# directory
			elif line[0] == '#':
				if has_dir:
					temp_dict[current_dir] = current_formats
					current_formats = []
					has_formats = False
				current_dir = line.split(' ')[1];
				has_dir = True

			# format
			elif line[0] == '-' and has_dir:
				current_formats.append(line.split(' ')[1])
				has_formats = True

			# last line
			if loop_counter == len(lines): 
				temp_dict[current_dir] = current_formats

		return temp_dict

	def scan_target_dir(self):
		temp_found_files = {}
		for key in self.conf_dict.keys():
			temp_found_files[key] = []

		files = os.listdir(self.target_dir_path)
		file_found = False

		for file in files:
			if os.path.isdir(file):
				continue

			file_found = False
			file_format = file.split('.')[-1]
			file_path = os.path.join(self.target_dir_path, file);

			for key in self.conf_dict.keys():
				if file_format in self.conf_dict[key]:
					temp_found_files[key].append(file_path)
					file_found = True
					break

			if file_found:
				self.found_files_counter += 1
				continue

			self.misc_files.append(file_path)
			self.misc_files_counter += 1
			self.found_files_counter += 1

		return temp_found_files

	def create_directories(self):
		for key in self.conf_dict.keys():
			if len(self.found_files[key]) > 0:
				dir_path = os.path.join(self.target_dir_path, key)
				try:
					os.mkdir(dir_path)
					self.created_folders_counter += 1
				except FileExistsError:
					continue

	def move_files(self):
		for key in self.conf_dict.keys():
			if len(self.found_files[key]) > 0:
				dir_path = os.path.join(self.target_dir_path, key)

				for file in self.found_files[key]:
					try:
						shutil.move(file, dir_path)
						self.moved_files_counter += 1
					except FileNotFoundError:
						failed_files_counter += 1

	def misc(self):
		try:
			dir_path = os.path.join(self.target_dir_path, "Misc")
			os.mkdir(dir_path)
			self.created_folders_counter += 1
		except FileExistsError:
			pass


		for file in self.misc_files:
			try:
				shutil.move(file, dir_path)
				self.moved_files_counter += 1
			except FileNotFoundError:
				self.failed_files_counter += 1

	def show_results(self):
		print("\nNew forlders:", self.created_folders_counter)
		print("Found: ", self.found_files_counter)
		print("Moved: ", self.moved_files_counter )
		print("Failed:", self.failed_files_counter)
		input("\nPress any key to finish")