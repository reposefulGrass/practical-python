# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost (filename):
	'Read the file \'filename\', then calculate the total cost.'

	total_cost = 0.0

	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(f)

		for row in rows:
			try:
				total_cost += (int(row[1]) * float(row[2].strip()))
			except ValueError:
				print("ParseError:", row)
				
	return total_cost

cost = round(portfolio_cost('Data/portfolio.csv'), 2)
print('Total cost', cost)

