#!/usr/bin/python3.8

# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost (filename):
	'Read the file \'filename\', then calculate the total cost.'

	total_cost = 0.0

	with open(filename, 'rt') as f:
		rows = csv.reader(f)

		headers = next(rows)
		for row in rows:
			try:
				cost = int(row[1]) * float(row[2].strip())
				total_cost += cost
			except ValueError:
				print("ParseError:", row)

	return total_cost


if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost = round(portfolio_cost(filename), 2)
print('Total cost', cost)

