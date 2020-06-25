#!/usr/bin/python3.8
# report.py
#
# Exercise 2.4

import sys
import csv


def read_prices (filename):
	'''
	Parses a .csv of the following format in quotes into a dictionary:
	"name,price"
	'''

	prices = {}

	with open(filename, 'rt') as f:
		rows = csv.reader(f)

		for row in rows:
			if len(row) == 2:
				name = row[0]
				price = float(row[1])
				prices[name] = price

	return prices


def read_portfolio (filename):
	'''
	Parses a .csv file of the following format in strings 
	into a portfolio: "name, shares, price"
	'''

	portfolio = []

	with open(filename, 'rt') as f:
		rows = csv.reader(f)

		headers = next(rows)
		for row in rows:
			record = dict(zip(headers, row))

			portfolio.append({
				'name': record['name'],
				'shares': int(record['shares']),
				'price': float(record['price'])
			})

	return portfolio


def make_report (portfolio, prices):
	'''
	Makes a report of the changes between a portfolio of stocks
	and the current prices of those stocks.
	'''

	report = []

	for row in portfolio:
		name = row['name']
		shares = row['shares']
		price = row['price']
		new_price = prices[name]
		change = round(new_price - price, 2)

		report.append((name, shares, new_price, change))

	return report


def print_report_header (headers):
	'''Prints the header for a report'''

	for column in headers:
		print(f'{column:>10s}', end=' ')
	print("")

	for i in range(0, len(headers)):
		print("%10s" % ('-' * 10), end=' ')
	print("")


def print_report ():
	print_report_header(('Name', 'Shares', 'Price', 'Change'))
	for name, shares, price, change in report:
		new_price = '$' + str(round(price, 2))
		print(f'{name:>10s} {shares:>10d} {new_price:>10s} {change:>10.2f}')


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

report = make_report(portfolio, prices)
print_report()



