# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv (filename, select=[], types=[]):
	''' Parse a csv file into a list of records '''

	with open(filename) as f:
		rows = csv.reader(f)
		
		headers = next(rows)
		records = []

		if select:
			indices = [headers.index(col) for col in select]	
			headers = select
		else:
			indices = []

		for row in rows:
			if len(row) == 0:
				continue

			if select:
				row = [row[index] for index in indices]
				if types:
					types = [types[index] for index in indices]

			record = {k: f(v) for k, v, f in zip(headers, row, types)}
			records.append(record)

	return records









