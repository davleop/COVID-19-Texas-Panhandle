# panhandle.py
import csv
import variables
import pandas as pd
from Find import Find
from sys import platform
from datetime import datetime

def write(filepath, headers, data):
	with open(filepath, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(headers)
		writer.writerows(data)

def main():
	counties = list(variables.counties)

	if platform == "win32":
		# IN
		active_path   = "Texas\\ActiveCaseData.xlsx"
		case_path     = "Texas\\CaseCountData.xlsx"
		test_path     = "Texas\\CumulativeTestTotals.xlsx"
		fatality_path = "Texas\\FatalityCountData.xlsx"
		cf_path       = "Texas\\CaseFatalCount.xlsx"
		new_case_path = "Texas\\NewCases.csv"

		# OUT
		active_out   = "Panhandle\\ActiveCaseData.csv"
		case_out     = "Panhandle\\CaseCountData.csv"
		test_out     = "Panhandle\\CumulativeTestTotals.csv"
		fatality_out = "Panhandle\\FatalityCountData.csv"
		cf_out       = "Panhandle\\CaseFatalCount.csv"
		new_case_out = "Panhandle\\NewCases.csv"
	else:
		# IN
		active_path   = "Texas/ActiveCaseData.xlsx"
		case_path     = "Texas/CaseCountData.xlsx"
		test_path     = "Texas/CumulativeTestTotals.xlsx"
		fatality_path = "Texas/FatalityCountData.xlsx"
		cf_path       = "Texas/CaseFatalCount.xlsx"
		new_case_path = "Texas/NewCases.csv"

		# OUT
		active_out   = "Panhandle/ActiveCaseData.csv"
		case_out     = "Panhandle/CaseCountData.csv"
		test_out     = "Panhandle/CumulativeTestTotals.csv"
		fatality_out = "Panhandle/FatalityCountData.csv"
		cf_out       = "Panhandle/CaseFatalCount.csv"
		new_case_out = "Panhandle/NewCases.csv"

	actives    = Find(active_path)
	cases      = Find(case_path)
	tests      = Find(test_path)
	fatalities = Find(fatality_path)
	cf         = Find(cf_path)

	
	actives.data(counties)
	cases.data(counties)
	tests.data(counties)
	fatalities.data(counties)
	cf.data(counties)

	actives.write(active_out)
	cases.write(case_out)
	tests.write(test_out)
	fatalities.write(fatality_out)
	cf.write(cf_out)

	#################################################
	# Process CSV file
	#################################################
	new_df = pd.read_csv(new_case_path)
	new_df.drop(['AttestationsDummy', '"Texas" Label', 'New Cases (copy)'], axis=1, inplace=True)
	new_df.rename(columns={'County':'county', 'Date':'date', 'New Cases':'cases'}, inplace=True)
	new_df.date = pd.to_datetime(new_df.date, format="%m/%d/%Y")
	new_df.set_index("date", inplace=True)
	new_df.to_csv("temp.csv")
	
	data = []
	with open("temp.csv", newline='') as f:
		reader = csv.reader(f)
		i = 0
		for row in reader:
			if i == 0:
				data.append(row)
				i += 1
			if row[1] in variables.counties:
				data.append(row)
	data = data[1:]

	dates = {}
	for i in data:
		dates[i[0]] = 0
	dates = list(dates.keys())

	headers = ['date'] + list(variables.counties)

	cases = []
	for day in dates:
		out = [0 for x in range(len(headers))]
		out[0] = day

		for lst in data:
			if lst[0] == day:
				out[headers.index(lst[1])] = lst[2]

		cases.append(out)

	write(new_case_out, headers, cases)


if __name__ == '__main__':
	main()