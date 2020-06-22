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
		for rowno, row in enumerate(rows):
			try:
				num_shares = int(row[1])
				price = float(row[2].strip())
				total_cost += (num_shares * price)
			except ValueError:
				print(f"Row {rowno}: Couldn't convert: {row}")

	return total_cost


if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost = round(portfolio_cost(filename), 2)
print('Total cost', cost)

