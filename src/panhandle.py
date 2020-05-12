# panhandle.py
from sys import exit
from Find import Find

def main():
	counties = ['Armstrong', 'Briscoe', 'Carson', 'Castro', 'Childress', 'Collingsworth', 'Dallam',
				'Deaf Smith', 'Donley', 'Gray', 'Hall', 'Hansford', 'Hartley', 'Hemphill','Hutchinson',
				'Lipscomb', 'Moore', 'Ochiltree', 'Oldham', 'Palmer', 'Potter', 'Randall', 'Roberts',
				'Sherman', 'Swisher', 'Wheeler']
	state = ['Texas']

	finder = Find("E:\\BoredProgrammer\\COVID-19\\covid-19-data\\us-counties.csv")
	texas_panhandle = finder.data(counties + state)

	finder.write("E:\\BoredProgrammer\\COVID-19\\Texas\\panhandle.csv")

if __name__ == '__main__':
	main()