# reformat.py
import pandas as pd
from sys import platform

def main():
	if platform == "win32":
		# IN
		active_path   = "Panhandle\\ActiveCaseData.csv"
		case_path     = "Panhandle\\CaseCountData.csv"
		test_path     = "Panhandle\\CumulativeTestTotals.csv"
		fatality_path = "Panhandle\\FatalityCountData.csv"
		cf_path       = "Texas\\CaseFatalCount.xlsx"

		# OUT
		active_out   = "Panhandle\\active.csv"
		case_out     = "Panhandle\\case.csv"
		test_out     = "Panhandle\\test.csv"
		fatality_out = "Panhandle\\fatality.csv"
		cf_out       = "Panhandle\\CaseFatalCount.csv"
	else:
		# IN
		active_path   = "Panhandle/ActiveCaseData.csv"
		case_path     = "Panhandle/CaseCountData.csv"
		test_path     = "Panhandle/CumulativeTestTotals.csv"
		fatality_path = "Panhandle/FatalityCountData.csv"
		cf_path       = "Texas/CaseFatalCount.xlsx"

		# OUT
		active_out   = "Panhandle/active.csv"
		case_out     = "Panhandle/case.csv"
		test_out     = "Panhandle/test.csv"
		fatality_out = "Panhandle/fatality.csv"
		cf_out       = "Panhandle/CaseFatalCount.csv"

	# Process Active Cases
	active_df = pd.read_csv(active_path)
	old_cols = active_df.columns.tolist()
	new_cols = ["date"]
	for date in old_cols[1:]:
		new_cols.append(date[:10])
	rename_dict = {i:j for i,j in zip(old_cols,new_cols)}
	active_df.rename(columns=rename_dict, inplace=True)
	active_df.set_index("date",inplace=True)
	active_df = active_df.T
	active_df.to_csv(active_out, index_label=active_df.index.name)

	# Process Case Counts
	case_df = pd.read_csv(case_path)
	case_df.drop(["Population"], axis=1, inplace=True)
	old_cols = case_df.columns.tolist()
	new_cols = ["date"]
	for date in old_cols[1:]:
		new_cols.append("2020-" + date[7:])
	rename_dict = {i:j for i,j in zip(old_cols,new_cols)}
	case_df.rename(columns=rename_dict, inplace=True)
	case_df.set_index("date",inplace=True)
	case_df = case_df.T
	case_df.to_csv(case_out)

	# Process Test Totals
	test_df = pd.read_csv(test_path,names=['county', 'tests'])
	test_df.to_csv(test_out, index=False)

	# Process Fatality Counts
	fatality_df = pd.read_csv(fatality_path)
	fatality_df.drop(["Population"], axis=1, inplace=True)
	old_cols = fatality_df.columns.tolist()
	new_cols = ['date']
	for date in old_cols[1:]:
		new_cols.append("2020-" + date[11:])
	rename_dict = {i:j for i,j in zip(old_cols,new_cols)}
	fatality_df.rename(columns=rename_dict, inplace=True)
	fatality_df.set_index("date",inplace=True)
	fatality_df = fatality_df.T
	fatality_df.to_csv(fatality_out)
	
if __name__ == '__main__':
	main()