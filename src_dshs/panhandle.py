# panhandle.py
from sys import platform
from Find import Find

def main():
	counties = ['Armstrong', 'Briscoe', 'Carson', 'Castro', 'Childress', 'Collingsworth', 'Dallam',
				'Deaf Smith', 'Donley', 'Gray', 'Hall', 'Hansford', 'Hartley', 'Hemphill','Hutchinson',
				'Lipscomb', 'Moore', 'Ochiltree', 'Oldham', 'Parmer', 'Potter', 'Randall', 'Roberts',
				'Sherman', 'Swisher', 'Wheeler']

	if platform == "win32":
		# IN
		active_path   = "Texas\\ActiveCaseData.xlsx"
		case_path     = "Texas\\CaseCountData.xlsx"
		test_path     = "Texas\\CumulativeTestTotals.xlsx"
		fatality_path = "Texas\\FatalityCountData.xlsx"

		# OUT
		active_out   = "Panhandle\\ActiveCaseData.csv"
		case_out     = "Panhandle\\CaseCountData.csv"
		test_out     = "Panhandle\\CumulativeTestTotals.csv"
		fatality_out = "Panhandle\\FatalityCountData.csv"
	else:
		# IN
		active_path   = "Texas/ActiveCaseData.xlsx"
		case_path     = "Texas/CaseCountData.xlsx"
		test_path     = "Texas/CumulativeTestTotals.xlsx"
		fatality_path = "Texas/FatalityCountData.xlsx"

		# OUT
		active_out   = "Panhandle/ActiveCaseData.csv"
		case_out     = "Panhandle/CaseCountData.csv"
		test_out     = "Panhandle/CumulativeTestTotals.csv"
		fatality_out = "Panhandle/FatalityCountData.csv"

	actives    = Find(active_path)
	cases      = Find(case_path)
	tests      = Find(test_path)
	fatalities = Find(fatality_path)

	
	actives.data(counties)
	cases.data(counties)
	tests.data(counties)
	fatalities.data(counties)

	actives.write(active_out)
	cases.write(case_out)
	tests.write(test_out)
	fatalities.write(fatality_out)
	

if __name__ == '__main__':
	main()