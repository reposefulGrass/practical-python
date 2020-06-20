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
				prices[name] = price

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


portfolio = portfolio_cost('Data/portfolio.csv')

total = 0.0
for s in portfolio:
	total += s['shares'] * s['price']

prices = read_prices('Data/prices.csv')

new_total = 0.0
for s in portfolio:
	new_total += s['shares'] * prices[s['name']]

result = round(new_total - total, 2)
if (result > 0):
	print("Gains:", result)
else:
	print("Losses:", result)

	
