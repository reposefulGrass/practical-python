#!/usr/bin/python3.8
# report.py
#
# Exercise 2.4

import sys
import csv


def read_prices (filename):
	'''Parses a .csv file into a dictionary'''
	prices = {}

	with open(filename, 'rt') as f:
		rows = csv.reader(f)

		for row in rows:
			if len(row) == 2:
				name = row[0]
				price = float(row[1])

	return prices


def portfolio_cost (filename):
	'''Parses a .csv file into a portfolio'''
	portfolio = []

	with open(filename, 'rt') as f:
		rows = csv.reader(f)

		headers = next(rows)
		for row in rows:
			name = row[0]
			shares = int(row[1])
			price = float(row[2])			

			portfolio.append({
				'name': name,
				'shares': shares,
				'price': price
			})

	return portfolio


if (sys.argv == 2):
	filename = argv[1]
else:
	filename = 'Data/portfolio.csv'	

portfolio = portfolio_cost(filename)

total = 0.0
for s in portfolio:
	total += s['shares'] * s['price']


print(total)


prices = read_prices('Data/prices.csv')
print(prices)
	
