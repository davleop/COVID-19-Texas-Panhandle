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
		active_path   = "Panhandle\\ActiveCaseData.csv"
		case_path     = "Panhandle\\CaseCountData.csv"
		test_path     = "Panhandle\\CumulativeTestTotals.csv"
		fatality_path = "Panhandle\\FatalityCountData.csv"
	else:
		active_path   = "Panhandle/ActiveCaseData.csv"
		case_apth     = "Panhandle/CaseCountData.csv"
		test_path     = "Panhandle/CumulativeTestTotals.csv"
		fatality_path = "Panhandle/FatalityCountData.csv"

	active_df   = pd.read_csv(active_path)
	case_df     = pd.read_csv(case_path)
	test_df     = pd.read_csv(test_path)
	fatality_df = pd.read_csv(fatality_path)

	plt.figure("Active Cases")

	plt.plot()

	plt.show()

if __name__ == '__main__':
	main()