# panhandle.py
from sys import exit
from Find import Find

def main():
	counties = ['Armstrong', 'Briscoe', 'Carson', 'Castro', 'Childress', 'Collingsworth', 'Dallam',
				'Deaf Smith', 'Donley', 'Gray', 'Hall', 'Hansford', 'Hartley', 'Hemphill','Hutchinson',
				'Lipscomb', 'Moore', 'Ochiltree', 'Oldham', 'Palmer', 'Potter', 'Randall', 'Roberts',
				'Sherman', 'Swisher', 'Wheeler']
	state = ['Texas']

	finder = Find("..\\covid-19-data\\us-counties.csv")
	texas_panhandle = finder.data(counties + state)

	finder.write("..\\Texas\\panhandle.csv")

if __name__ == '__main__':
	main()