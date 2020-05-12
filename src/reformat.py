# reformat.py
import csv
from sys import platform

def write(filepath, headers, data):
	with open(filepath, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(headers)
		writer.writerows(data)

def main():
	headers  = ['date', 'Armstrong', 'Briscoe', 'Carson', 'Castro', 'Childress', 'Collingsworth', 
				'Dallam', 'Deaf Smith', 'Donley', 'Gray', 'Hall', 'Hansford', 'Hartley', 'Hemphill', 
				'Hutchinson', 'Lipscomb', 'Moore', 'Ochiltree', 'Oldham', 'Palmer', 'Potter', 
				'Randall', 'Roberts', 'Sherman', 'Swisher', 'Wheeler']
	
	if platform == "win32":
		filepath = "..\\Texas\\panhandle.csv"
		deathout = "..\\Texas\\panhandle_deaths.csv"
		casesout = "..\\Texas\\panhandle_cases.csv"
	else:
		filepath = "../Texas/panhandle.csv"
		deathout = "../Texas/panhandle_deaths.csv"
		casesout = "../Texas/panhandle_cases.csv"

	data = []

	with open(filepath, newline='') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			data.append(row)
	data = data[1:]

	dates = {}
	for i in data:
		dates[i[0]] = 0
	dates = list(dates.keys())

	cases = []
	for day in dates:
		out = [0 for x in range(len(headers))]
		out[0] = day

		for lst in data:
			if lst[0] == day:
				out[headers.index(lst[1])] = lst[4]

		cases.append(out)

	deaths = []
	for day in dates:
		out = [0 for x in range(len(headers))]
		out[0] = day

		for lst in data:
			if lst[0] == day:
				out[headers.index(lst[1])] = lst[5]

		deaths.append(out)

	write(casesout, headers, cases)
	write(deathout, headers, deaths)

if __name__ == '__main__':
	main()