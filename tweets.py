import re

class Cleaner:

	def __init__(self, line, file):
		self.line = line
		self.file = file


	#cleans the starting numbers and spaces in the beginning of each line
		
	def clean_initial_junk(self):
		
		counter = 0
		for ch in self.line:
			if ch.isalpha() == False:
				counter+=1 
			else:
				break			
		self.line = self.line[counter: ]
			
	# removes emojis and other characters like .......	
	def	clean_emojis(self):

		pattern = re.findall(r'[.:\-)(]+', self.line)

		for match in pattern:
	
			self.line = self.line.replace(match, "")

	# replaces @name with **NAME**		
	def clean_atTheRate(self):
	

		pattern = re.findall(r'@\w+', self.line)

		for match in pattern:
			self.line = self.line.replace(match, "**NAME**")


	# removes redundant white spaces		
	def clean_extra_spaces(self):

		
		self.line = " ".join( self.line.split())
		
	
				
	# find, separates and replace the joined words(e.g. feelBlue) with separate words(e.g. feel Blue)
	def deal_hash(self):

		pattern = re.findall(r'#[a-zA-z]\w*', self.line)

		for match in pattern:
			words = re.findall(r'[A-Za-z][a-z]*', match)
			word = " ".join(words)
			self.line = self.line.replace(match, word)



			

	# writes the edited line to the file passed 		
	def write_line(self):

		self.file.write(self.line)







with open('jan9-2012.txt', 'r') as f:
	f1 = open('clean.txt', 'w')
	
	line = f.readline()

	# iterates over the file line by line
	while line > 0:

		clean_line = Cleaner(line, f1)

		clean_line.clean_initial_junk()

		clean_line.clean_emojis()

		clean_line.clean_atTheRate()

		clean_line.deal_hash()

		clean_line.clean_extra_spaces()

		clean_line.write_line()

		f1.write('\n')

		line = f.readline()

	f1.close()