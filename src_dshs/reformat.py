# reformat.py
import csv
from sys import platform
import pandas as pd

def main():
	if platform == "win32":
		# IN
		active_path   = "Panhandle\\ActiveCaseData.csv"
		case_path     = "Panhandle\\CaseCountData.csv"
		test_path     = "Panhandle\\CumulativeTestTotals.csv"
		fatality_path = "Panhandle\\FatalityCountData.csv"

		# OUT
		active_out   = "Panhandle\\active.csv"
		case_out     = "Panhandle\\case.csv"
		test_out     = "Panhandle\\test.csv"
		fatality_out = "Panhandle\\fatality.csv"
	else:
		# IN
		active_path   = "Panhandle/ActiveCaseData.csv"
		case_path     = "Panhandle/CaseCountData.csv"
		test_path     = "Panhandle/CumulativeTestTotals.csv"
		fatality_path = "Panhandle/FatalityCountData.csv"

		# OUT
		active_out   = "Panhandle/active.csv"
		case_out     = "Panhandle/case.csv"
		test_out     = "Panhandle/test.csv"
		fatality_out = "Panhandle/fatality.csv"

	# Process Active Cases
	active_df = pd.read_csv(active_path)
	old_cols = active_df.columns.tolist()
	new_cols = ["date"]
	for date in old_cols[1:]:
		new_cols.append(date[:10])
	rename_dict = {i:j for i,j in zip(old_cols,new_cols)}
	active_df.rename(columns=rename_dict, inplace=True)
	active_df = active_df.T
	active_df.to_csv(active_out)

	# Process Case Counts
	case_df = pd.read_csv(case_path)
	case_df = case_df.replace(r'Cases  ','', regex=True)
	case_df = case_df.T
	case_df.drop(case_df.index[[0]], inplace=True)
	case_df.to_csv(case_out, index=False)

	# Process Test Totals
	test_df = pd.read_csv(test_path)
	test_df = test_df.replace(r' 00:00:00','', regex=True)
	test_df = test_df.T
	test_df.drop(test_df.index[[0]], inplace=True)
	test_df.to_csv(test_out, index=False)

	# Process Fatality Counts
	fatality_df = pd.read_csv(fatality_path)
	fatality_df = fatality_df.replace(r' 00:00:00','', regex=True)
	fatality_df = fatality_df.T
	fatality_df.drop(fatality_df.index[[0]], inplace=True)
	fatality_df.to_csv(fatality_out, index=False)

if __name__ == '__main__':
	main()