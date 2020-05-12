# panhandle.py
from sys import platform
from sys import exit
from Find import Find

def main():
	counties = ['Armstrong', 'Briscoe', 'Carson', 'Castro', 'Childress', 'Collingsworth', 'Dallam',
				'Deaf Smith', 'Donley', 'Gray', 'Hall', 'Hansford', 'Hartley', 'Hemphill','Hutchinson',
				'Lipscomb', 'Moore', 'Ochiltree', 'Oldham', 'Palmer', 'Potter', 'Randall', 'Roberts',
				'Sherman', 'Swisher', 'Wheeler']
	state = ['Texas']

	if platform == "win32":
		counties_path = "covid-19-data\\us-counties.csv"
		panhandle = "Texas\\panhandle.csv"
	else:
		counties_path = "covid-19-data/us-counties.csv"
		panhandle = "Texas/panhandle.csv"

	finder = Find(counties_path)
	texas_panhandle = finder.data(counties + state)

	finder.write()

if __name__ == '__main__':
	main()