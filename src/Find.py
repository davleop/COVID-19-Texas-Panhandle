# Find.py
import csv

class Find:
	def __init__(self, filepath):
		self.filepath = filepath
		self.out = []

	def data(self, keywords=[]):
		if len(keywords) == 0:
			# just return all the data
			with open(self.filepath, newline='') as csvfile:
				reader = csv.reader(csvfile)
				i = 0
				for row in reader:
					if i == 0:
						self.out.append(row)
						i += 1
					self.out.append(row)
		else:
			# return the data with only the keywords
			with open(self.filepath, newline='') as csvfile:
				reader = csv.reader(csvfile)
				i = 0
				for row in reader:
					if i == 0:
						self.out.append(row)
						i += 1
					if row[1] in keywords and row[2] in keywords:
						self.out.append(row)

		return self.out

	def write(self, filepath='.\\out.csv'):
		# writes the out put of data into a csv file
		with open(filepath, 'w', newline='') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerows(self.out)