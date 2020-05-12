# graph.py
import warnings
from sys import platform
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# *** ignoring MatplotlibDeprecationWarning *** #
warnings.filterwarnings("ignore")
# ********************************************* #

def main():
	if platform == "win32":
		cases_path = "..\\Texas\\panhandle_cases.csv"
		deaths_path = "..\\Texas\\panhandle_deaths.csv"
	else:
		cases_path = "../Texas/panhandle_cases.csv"
		deaths_path = "../Texas/panhandle_deaths.csv"

	counties = ['Armstrong', 'Briscoe', 'Carson', 'Castro', 'Childress', 'Collingsworth', 'Dallam',
				'Deaf Smith', 'Donley', 'Gray', 'Hall', 'Hansford', 'Hartley', 'Hemphill','Hutchinson',
				'Lipscomb', 'Moore', 'Ochiltree', 'Oldham', 'Palmer', 'Potter', 'Randall', 'Roberts',
				'Sherman', 'Swisher', 'Wheeler']

	cases_df = pd.read_csv(cases_path)
	deaths_df = pd.read_csv(deaths_path)

	plt.figure("Cases")

	for county in counties:
		plt.plot(cases_df.date, cases_df[county])
	
	plt.ylabel("# of Cases")

	plt.xlabel("Day")
	ax = plt.axes()
	plt.xticks(rotation=45)

	plt.title("Texas Panhandle Cases\nLast updated: " + cases_df.date.iloc[-1])
	plt.legend(counties)

	###################################################
	plt.figure("Deaths")

	for county in counties:
		plt.plot(cases_df.date, deaths_df[county])
	
	plt.ylabel("# of Deaths")

	plt.xlabel("Day")
	plt.xticks(rotation=45)

	plt.title("Texas Panhandle Deaths\nLast updated: " + deaths_df.date.iloc[-1])
	plt.legend(counties)

	plt.show()

if __name__ == '__main__':
	main()