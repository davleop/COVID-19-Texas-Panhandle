# Find.py
import csv
import pandas as pd
import numpy as np

class Find:
	def __init__(self, filepath):
		self.filepath = filepath
		self.out = []

	def data(self, keywords=[]):
		if len(keywords) == 0:
			# just return all the data
			df = pd.read_excel(self.filepath)
			df.drop(df.index[[0]], inplace=True)
			df.columns = df.iloc[1]
			df.reset_index(inplace=True, drop=True)
			df = df.loc[:, df.columns.notnull()]
			df = df.replace(r'\n',' ',regex=True)
			df.to_csv("temp.csv", index=False)

			with open("temp.csv", newline='') as csvfile:
				reader = csv.reader(csvfile)
				i = 0
				for row in reader:
					if i == 0:
						i += 1
						continue
					self.out.append(row)

		else:
			# return the data with only the keywords
			df = pd.read_excel(self.filepath)
			df.drop(df.index[[0]], inplace=True)
			df.columns = df.iloc[1]
			df.reset_index(inplace=True, drop=True)
			df = df.loc[:, df.columns.notnull()]
			df = df.replace(r'\n',' ',regex=True)
			df.to_csv("temp.csv", index=False)

			with open("temp.csv", newline='') as csvfile:
				reader = csv.reader(csvfile)
				i = 0
				for row in reader:
					if i == 0:
						i += 1
						continue
					if i == 1:
						self.out.append(row)
						i += 1
					if row[0] in keywords:
						self.out.append(row)

		return self.out

	def write(self, filepath='out.csv'):
		# writes the out put of data into a csv file
		with open(filepath, 'w', newline='') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerows(self.out)