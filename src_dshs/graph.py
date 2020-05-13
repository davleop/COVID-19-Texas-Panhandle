# graph.py
import warnings
from sys import platform
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from Data import Data
from sys import setrecursionlimit

# *** ignoring MatplotlibDeprecationWarning *** #
warnings.filterwarnings("ignore")
# ********************************************* #

# *** SET NEW RECURSION LIMIT *** #
setrecursionlimit(10000)
# ******************************* #

def main():
	if platform == "win32":
		active_path   = "Panhandle\\active.csv"
		case_path     = "Panhandle\\case.csv"
		fatality_path = "Panhandle\\fatality.csv"
	else:
		active_path   = "Panhandle/active.csv"
		case_apth     = "Panhandle/case.csv"
		fatality_path = "Panhandle/fatality.csv"
	
	active_df   = pd.read_csv(active_path, index_col=0)
	case_df     = pd.read_csv(case_path, index_col=0)
	fatality_df = pd.read_csv(fatality_path, index_col=0)

	df_list = [
		Data(active_df,"Active Cases","Day","# of Active Cases","Active Cases Across the Texas Panhandle\nLast updated: " + active_df.index[-1]), 
		Data(case_df,"Cases","Day","# of Cases","Case Counts Across the Texas Panhandle\nLast updated: " + case_df.index[-1]),
		Data(fatality_df,"Fatalities","Day","# of Fatalities","Fatalities Across the Texas Panhandle\nLast update: " + str(fatality_df.index[-1]))
	]

	# Plot general panhandle graphs
	for d_obj in df_list:
		counties = ['Armstrong', 'Briscoe', 'Carson', 'Castro', 'Childress', 'Collingsworth', 'Dallam',
					'Deaf Smith', 'Donley', 'Gray', 'Hall', 'Hansford', 'Hartley', 'Hemphill','Hutchinson',
					'Lipscomb', 'Moore', 'Ochiltree', 'Oldham', 'Palmer', 'Potter', 'Randall', 'Roberts',
					'Sherman', 'Swisher', 'Wheeler']

		m = plt.figure(d_obj.figure, figsize=(12.0, 8.5))
		ax = m.gca()
		ax.yaxis.set_major_locator(MaxNLocator(integer=True))

		plt.xlabel(d_obj.xlabel)
		plt.ylabel(d_obj.ylabel)

		not_found = []
		for county in counties:
			try:
				plt.plot(d_obj.df[county])
			except:
				not_found.append(county)
				print("County not found: " + county)

		for county in not_found:
			counties.pop(counties.index(county))

		plt.xticks(rotation=90)

		plt.title(d_obj.title)
		plt.legend(counties)
		plt.savefig("graphs/" + d_obj.figure.replace(' ', '') + ".png")
		plt.savefig("png/" + d_obj.figure.replace(' ', '') + ".png")

	counties = ['Armstrong', 'Briscoe', 'Carson', 'Castro', 'Childress', 'Collingsworth', 'Dallam',
				'Deaf Smith', 'Donley', 'Gray', 'Hall', 'Hansford', 'Hartley', 'Hemphill','Hutchinson',
				'Lipscomb', 'Moore', 'Ochiltree', 'Oldham', 'Palmer', 'Potter', 'Randall', 'Roberts',
				'Sherman', 'Swisher', 'Wheeler']
	
	# Plot individual counties Actives
	for county in counties:
		try:
			active_df[county]
			m = plt.figure("Active Cases for " + county, figsize=(12.0, 8.5))
			ax = m.gca()
			ax.yaxis.set_major_locator(MaxNLocator(integer=True))

			plt.xlabel("Day")
			plt.ylabel("# of Active Cases")

			plt.plot(active_df[county])

			plt.xticks(rotation=90)

			plt.title("Active Cases for " + county + " County")
			plt.savefig("graphs/Active" + county.replace(' ', '') + ".png")
		except:
			print("County not found: " + county)

	# Plot individual counties Case Counts
	for county in counties:
		try:
			case_df[county]
			m = plt.figure("Case Count for " + county, figsize=(12.0, 8.5))
			ax = m.gca()
			ax.yaxis.set_major_locator(MaxNLocator(integer=True))

			plt.xlabel("Day")
			plt.ylabel("# of Cases")

			plt.plot(case_df[county])

			plt.xticks(rotation=90)

			plt.title("Case Count for " + county + " County")
			plt.savefig("graphs/CaseCount" + county.replace(' ', '') + ".png")
		except:
			print("County not found: " + county)

	# Plot individual counties Fatalities
	for county in counties:
		try:
			fatality_df[county]
			m = plt.figure("Fatalities for " + county, figsize=(12.0, 8.5))
			ax = m.gca()
			ax.yaxis.set_major_locator(MaxNLocator(integer=True))

			plt.xlabel("Day")
			plt.ylabel("# of Fatalities")

			plt.plot(fatality_df[county])

			plt.xticks(rotation=90)

			plt.title("Fatalities for " + county + " County")
			plt.savefig("graphs/Fatalities" + county.replace(' ', '') + ".png")
		except:
			print("County not found: " + county)

if __name__ == '__main__':
	main()