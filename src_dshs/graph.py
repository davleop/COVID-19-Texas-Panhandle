# graph.py
import csv
import math
import warnings
import variables
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sys import exit
from Data import Data
from sys import platform
from datetime import datetime
from datetime import timedelta
from sys import setrecursionlimit
from matplotlib.ticker import MaxNLocator

# *** ignoring MatplotlibDeprecationWarning *** #
warnings.filterwarnings("ignore")
# ********************************************* #

# *** SET NEW RECURSION LIMIT *** #
setrecursionlimit(10000)
# ******************************* #

def calculate_sizes(lst):
	out = []
	for i in lst[1:]:
		out.append(math.ceil(math.sqrt(int(i) / math.pi)) * variables.MULTIPLIER)

	return np.array(out)

def main():
	if platform == "win32":
		active_path   = "Panhandle\\active.csv"
		case_path     = "Panhandle\\case.csv"
		fatality_path = "Panhandle\\fatality.csv"
		cf_path       = "Panhandle\\CaseFatalCount.csv"
		new_case_path = "Panhandle\\NewCases.csv"
		panhandle_img = "png\\panhandle.png"
	else:
		active_path   = "Panhandle/active.csv"
		case_path     = "Panhandle/case.csv"
		fatality_path = "Panhandle/fatality.csv"
		cf_path       = "Panhandle/CaseFatalCount.csv"
		new_case_path = "Panhandle/NewCases.csv"
		panhandle_img = "png/panhandle.png"

	active_df   = pd.read_csv(active_path, index_col=0)
	case_df     = pd.read_csv(case_path, index_col=0)
	fatality_df = pd.read_csv(fatality_path, index_col=0)
	cf_df       = pd.read_csv(cf_path, names=['county','cases','fatalities'])
	new_df		= pd.read_csv(new_case_path, index_col=0)

	df_list = [
		Data(active_df,"Active Cases Estimate","Day","# of Active Cases Estimate","Active Cases Estimate Across the Texas Panhandle\nLast updated: " + active_df.index[-1]), 
		Data(case_df,"Cases","Day","# of Cases","Case Counts Across the Texas Panhandle\nLast updated: " + case_df.index[-1]),
		Data(fatality_df,"Fatalities","Day","# of Fatalities","Fatalities Across the Texas Panhandle\nLast update: " + str(fatality_df.index[-1]))
	]

	##############################################################################
	# Plot general panhandle graphs                                              #
	##############################################################################
	for d_obj in df_list:
		counties = list(variables.counties)

		m = plt.figure(d_obj.figure, figsize=variables.figSize)
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
			m = plt.figure("Active Cases Estimate for " + county, figsize=variables.figSize)
			ax = m.gca()
			ax.yaxis.set_major_locator(MaxNLocator(integer=True))

			plt.xlabel("Day")
			plt.ylabel("# of Active Cases Estimate")

			plt.plot(active_df[county])

			plt.xticks(rotation=90)

			plt.title("Active Cases Estimate for " + county + " County")
			plt.savefig("graphs/ActiveEstimate" + county.replace(' ', '') + ".png")
		except:
			print("County not found: " + county)

	##############################################################################
	# Plot individual counties Case Counts                                       #
	##############################################################################
	for county in counties:
		try:
			case_df[county]
			m = plt.figure("Case Count for " + county, figsize=variables.figSize)
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
			m = plt.figure("Fatalities for " + county, figsize=variables.figSize)
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
	m = plt.figure(RP_aggregate + " Active Cases Estimate", figsize=(12.0,8.5))
	ax = m.gca()
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))

	plt.xlabel("Day")
	plt.ylabel("# of Active Cases Estimate")

	plt.plot(active_df[RP_aggregate])
	plt.xticks(rotation=90)

	plt.title("Active Cases Estimate for " + RP_aggregate)
	plt.savefig("graphs/ActiveEstimate" + RP_aggregate + ".png")

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

	new_df[RP_aggregate] = new_df[randall] + new_df[potter]
	m = plt.figure(RP_aggregate + " New Cases", figsize=(12.0,8.5))
	ax = m.gca()
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))

	plt.xlabel("Day")
	plt.ylabel("# of New Cases")

	plt.plot(new_df[RP_aggregate])
	plt.xticks(rotation=90)

	plt.title("New Cases for " + RP_aggregate)
	plt.savefig("graphs/NewCases" + RP_aggregate + ".png")


	##############################################################################
	# Panhandle aggregate                                                        #
	##############################################################################
	agg = 'aggregate'
	active_df[agg]   = 0
	case_df[agg]     = 0
	fatality_df[agg] = 0
	new_df[agg]      = 0
	
	for county in variables.counties:
		active_df[agg] += active_df[county]
		case_df[agg] += case_df[county]
		fatality_df[agg] += fatality_df[county]
		new_df[agg] += new_df[county]

	df_list = [
		Data(active_df,"Active Cases Estimate Aggregated","Day","# of Active Cases Estimate","Active Cases Estimate Across the Texas Panhandle Aggregated\nLast updated: " + active_df.index[-1]), 
		Data(case_df,"Cases Aggregated","Day","# of Cases","Case Counts Across the Texas Panhandle Aggregated\nLast updated: " + case_df.index[-1]),
		Data(fatality_df,"Fatalities Aggregated","Day","# of Fatalities","Fatalities Across the Texas Panhandle Aggregated\nLast update: " + str(fatality_df.index[-1])),
		Data(new_df,"New Cases Aggregated","Day","# of New Cases","New Cases Across the Texas Panhandle Aggregated\nLast update: " + str(new_df.index[-1]))
	]

	for df in df_list:
		m = plt.figure(df.figure, figsize=variables.figSize)
		ax = m.gca()
		ax.yaxis.set_major_locator(MaxNLocator(integer=True))

		plt.xlabel(df.xlabel)
		plt.ylabel(df.ylabel)

		plt.plot(df.df[agg])
		plt.xticks(rotation=90)

		plt.title(df.title)
		plt.savefig("graphs/" + df.figure.replace(' ', '') + ".png")
		plt.savefig("png/" + df.figure.replace(' ', '') + ".png")

	for df in df_list:
		m = plt.figure(df.figure + " Bar", figsize=variables.figSize)
		ax = m.gca()
		ax.yaxis.set_major_locator(MaxNLocator(integer=True))

		plt.xlabel(df.xlabel)
		plt.ylabel(df.ylabel)

		plt.bar(df.df.index,df.df[agg])
		plt.xticks(rotation=90)

		plt.title(df.title)
		plt.savefig("graphs/" + df.figure.replace(' ', '') + "Bar.png")
		plt.savefig("png/" + df.figure.replace(' ', '') + "Bar.png")

	

	##############################################################################
	# Graph recovered cases
	# From what I can tell, recoveries should be calculated as so:
	# 	Recoveries = Cases - Active Cases - Fatalities
	# *** IF THIS IS WRONG, PLEASE CORRECT ME BY SUBMITTING AN ISSUE OR ***
	# *** OR DO A PULL REQUEST CORRECTING THE ISSUE                     ***   
	# *** I DO BELIEVE THIS IS WRONG. PLEASE BE CAREFUL                 ***
	##############################################################################
	headers = list(variables.counties)
	headers.append("Randall+Potter")
	headers.append("aggregate")

	cp_case_df     = case_df.copy()
	cp_fatality_df = fatality_df.copy()

	dta = datetime.strptime(active_df.index[0], '%Y-%m-%d')
	dtc = datetime.strptime(cp_case_df.index[0], '%Y-%m-%d')
	delta = dta - dtc
	days = int(delta.days)

	cp_case_df = cp_case_df.iloc[days-3:]
	cp_fatality_df = cp_fatality_df[days:]

	cp_fatality_df.set_index(cp_case_df.index, inplace=True)
	recoveries = cp_case_df - active_df - cp_fatality_df

	for county in headers:
		try:
			recoveries[county]
			m = plt.figure("Recoveries: " + county, figsize=variables.figSize)
			ax = m.gca()
			ax.yaxis.set_major_locator(MaxNLocator(integer=True))

			plt.xlabel("Day")
			plt.ylabel("# of Recoveries")

			plt.plot(recoveries[county])

			plt.xticks(rotation=90)

			plt.title("Recoveries: " + county)
			plt.savefig("graphs/Recoveries" + county.replace(' ', '') + ".png")
		except:
			print("County not found: " + county)

	m = plt.figure("Recoveries for the Texas Panhandle", figsize=variables.figSize)
	ax = m.gca()
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))

	plt.xlabel("Day")
	plt.ylabel("# of Recoveries")

	for county in variables.counties:
		plt.plot(recoveries[county])

	plt.xticks(rotation=90)

	plt.title("Recoveries for the Texas Panhandle\n(may not be accurate due to descrepancies in data collection)")
	plt.legend(variables.counties)
	plt.savefig("graphs/Recoveries.png")

	##############################################################################
	# Fatalities bar graph
	##############################################################################
	plt.figure("Fatalities by County", figsize=variables.figSize)
	ax = m.gca()
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.xlabel("County")
	plt.ylabel("# of Fatalities")
	plt.bar(cf_df.county, cf_df.fatalities)
	plt.xticks(rotation=90)
	plt.title("Fatalities by County\nLast updated: " + fatality_df.index[-1])
	plt.savefig("graphs/FatalitiesBar.png")
	plt.savefig("png/FatalitiesBar.png")

	##############################################################################
	# Cases bar graph
	##############################################################################
	plt.figure("Cases by County", figsize=variables.figSize)
	ax = m.gca()
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.xlabel("County")
	plt.ylabel("# of Cases")
	plt.bar(cf_df.county, cf_df.cases)
	plt.xticks(rotation=90)
	plt.title("Cases by County\nLast updated: " + case_df.index[-1])
	plt.savefig("graphs/CasesBar.png")
	plt.savefig("png/CasesBar.png")

	##############################################################################
	# Graph of panhandle with circles correlated to cases, fatalities, etc.
	##############################################################################
	plt.figure("Panhandle Case Count")
	im = plt.imread(panhandle_img)
	implot = plt.imshow(im)

	x = np.array(variables.x)
	y = np.array(variables.y)
	s = calculate_sizes(cf_df.cases.tolist())

	plt.scatter(x,y,s=s,color='r',alpha=0.5)

	plt.gca().axes.get_xaxis().set_visible(False)
	plt.gca().axes.get_yaxis().set_visible(False)
	plt.title("Panhandle Case Counts\nLast updated: " + datetime.now().strftime("%Y-%m-%d"))
	plt.savefig("graphs/PanhandleCases.png")
	plt.savefig("png/PanhandleCases.png")

	plt.figure("Panhandle Fatalities")
	im = plt.imread(panhandle_img)
	implot = plt.imshow(im)

	x = np.array(variables.x)
	y = np.array(variables.y)
	s = calculate_sizes(cf_df.fatalities.tolist())

	plt.scatter(x,y,s=s,color='b',alpha=0.5)

	plt.gca().axes.get_xaxis().set_visible(False)
	plt.gca().axes.get_yaxis().set_visible(False)
	plt.title("Panhandle Fatalities\nLast updated: " + datetime.now().strftime("%Y-%m-%d"))
	plt.savefig("graphs/PanhandleFatalities.png")
	plt.savefig("png/PanhandleFatalities.png")

	##############################################################################
	# Graph number of new of cases per day
	##############################################################################
	m = plt.figure("New Cases Bar", figsize=variables.figSize)
	ax = m.gca()
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))

	plt.xlabel("Day")
	plt.ylabel("# of New Cases")

	for county in variables.counties:
		plt.bar(new_df.index,new_df[county])

	plt.xticks(rotation=90)

	plt.title("New Cases for the Texas Panhandle\nLast updated: " + new_df.index[-1])
	plt.legend(variables.counties)
	plt.savefig("graphs/NewCasesBar.png")
	plt.savefig("png/NewCasesBar.png")

	m = plt.figure("New Cases", figsize=variables.figSize)
	ax = m.gca()
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))

	plt.xlabel("Day")
	plt.ylabel("# of New Cases")

	for county in variables.counties:
		plt.plot(new_df[county])

	plt.xticks(rotation=90)

	plt.title("New Cases for the Texas Panhandle\nLast updated: " + new_df.index[-1])
	plt.legend(variables.counties)
	plt.savefig("graphs/NewCases.png")
	plt.savefig("png/NewCases.png")

	for county in variables.counties:
		try:
			new_df[county]
			m = plt.figure("New Cases: " + county, figsize=variables.figSize)
			ax = m.gca()
			ax.yaxis.set_major_locator(MaxNLocator(integer=True))

			plt.xlabel("Day")
			plt.ylabel("# of New Cases")

			plt.plot(new_df[county])

			plt.xticks(rotation=90)

			plt.title("New Cases: " + county)
			plt.savefig("graphs/NewCases" + county.replace(' ', '') + ".png")
		except:
			print("County not found: " + county)

	for county in variables.counties:
		try:
			new_df[county]
			m = plt.figure("New Cases: " + county + " Bar", figsize=variables.figSize)
			ax = m.gca()
			ax.yaxis.set_major_locator(MaxNLocator(integer=True))

			plt.xlabel("Day")
			plt.ylabel("# of New Cases")

			plt.bar(new_df.index,new_df[county])

			plt.xticks(rotation=90)

			plt.title("New Cases: " + county)
			plt.savefig("graphs/NewCases" + county.replace(' ', '') + "Bar.png")
		except:
			print("County not found: " + county)

	# TODO(David): Forecasting/Trend Analysis?
	active_df.index = pd.to_datetime(active_df.index)
	case_df.index = pd.to_datetime(case_df.index)
	fatality_df.index = pd.to_datetime(fatality_df.index)
	new_df.index = pd.to_datetime(new_df.index)

if __name__ == '__main__':
	main()