# graph.py
import warnings
from sys import platform
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from Data import Data
from sys import setrecursionlimit
import variables

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
		case_path     = "Panhandle/case.csv"
		fatality_path = "Panhandle/fatality.csv"
	
	active_df   = pd.read_csv(active_path, index_col=0)
	case_df     = pd.read_csv(case_path, index_col=0)
	fatality_df = pd.read_csv(fatality_path, index_col=0)

	df_list = [
		Data(active_df,"Active Cases","Day","# of Active Cases","Active Cases Across the Texas Panhandle\nLast updated: " + active_df.index[-1]), 
		Data(case_df,"Cases","Day","# of Cases","Case Counts Across the Texas Panhandle\nLast updated: " + case_df.index[-1]),
		Data(fatality_df,"Fatalities","Day","# of Fatalities","Fatalities Across the Texas Panhandle\nLast update: " + str(fatality_df.index[-1]))
	]

	##############################################################################
	# Plot general panhandle graphs                                              #
	##############################################################################
	for d_obj in df_list:
		counties = list(variables.counties)

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

	##############################################################################
	# Plot individual counties Actives                                           #
	##############################################################################
	for county in variables.counties:
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

	##############################################################################
	# Plot individual counties Case Counts                                       #
	##############################################################################
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

	##############################################################################
	# Plot individual counties Fatalities                                        #
	##############################################################################
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

	##############################################################################			
	# Aggregate Randall and Potter County.                                       #
	##############################################################################
	randall = "Randall"
	potter  = "Potter"
	RP_aggregate = "Randall+Potter"
	active_df[RP_aggregate] = active_df[randall] + active_df[potter]
	m = plt.figure(RP_aggregate + " Active Cases", figsize=(12.0,8.5))
	ax = m.gca()
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))

	plt.xlabel("Day")
	plt.ylabel("# of Active Cases")

	plt.plot(active_df[RP_aggregate])
	plt.xticks(rotation=90)

	plt.title("Active Cases for " + RP_aggregate)
	plt.savefig("graphs/Active" + RP_aggregate + ".png")

	case_df[RP_aggregate] = case_df[randall] + case_df[potter]
	m = plt.figure(RP_aggregate + " Case Count", figsize=(12.0,8.5))
	ax = m.gca()
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))

	plt.xlabel("Day")
	plt.ylabel("# of Cases")

	plt.plot(case_df[RP_aggregate])
	plt.xticks(rotation=90)

	plt.title("Case Count for " + RP_aggregate)
	plt.savefig("graphs/CaseCount" + RP_aggregate + ".png")

	fatality_df[RP_aggregate] = fatality_df[randall] + fatality_df[potter]
	m = plt.figure(RP_aggregate + " Fatalities", figsize=(12.0,8.5))
	ax = m.gca()
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))

	plt.xlabel("Day")
	plt.ylabel("# of Fatalities")

	plt.plot(fatality_df[RP_aggregate])
	plt.xticks(rotation=90)

	plt.title("Fatalities for " + RP_aggregate)
	plt.savefig("graphs/Fatalities" + RP_aggregate + ".png")

	##############################################################################
	# Panhandle aggregate                                                        #
	##############################################################################
	agg = 'aggregate'
	active_df[agg]   = 0
	case_df[agg]     = 0
	fatality_df[agg] = 0 
	
	for county in variables.counties:
		active_df[agg] += active_df[county]
		case_df[agg] += case_df[county]
		fatality_df[agg] += fatality_df[county]

	df_list = [
		Data(active_df,"Active Cases Aggregated","Day","# of Active Cases","Active Cases Across the Texas Panhandle Aggregated\nLast updated: " + active_df.index[-1]), 
		Data(case_df,"Cases Aggregated","Day","# of Cases","Case Counts Across the Texas Panhandle Aggregated\nLast updated: " + case_df.index[-1]),
		Data(fatality_df,"Fatalities Aggregated","Day","# of Fatalities","Fatalities Across the Texas Panhandle Aggregated\nLast update: " + str(fatality_df.index[-1]))
	]

	for df in df_list:
		m = plt.figure(df.figure, figsize=(12.0, 8.5))
		ax = m.gca()
		ax.yaxis.set_major_locator(MaxNLocator(integer=True))

		plt.xlabel(df.xlabel)
		plt.ylabel(df.ylabel)

		plt.plot(df.df[agg])
		plt.xticks(rotation=90)

		plt.title(df.title)
		plt.savefig("graphs/" + df.figure.replace(' ', '') + ".png")
		plt.savefig("png/" + df.figure.replace(' ', '') + ".png")

	##############################################################################
	# TODO(David): Graph recovered cases
	# From what I can tell, recoveries should be calculated as so:
	# 	Recoveries = Cases - Active Cases - Fatalities
	##############################################################################


	# TODO(David): Graph rate of inc/dec of cases per day
	# TODO(David): Make graph of panhandle with circles correlated to cases, fatalities, etc.
	# TODO(David): Forecasting/Trend Analysis?


if __name__ == '__main__':
	main()