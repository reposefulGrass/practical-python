# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv (filename, select=[], types=[], has_headers=True):
	''' Parse a csv file into a list of records '''

	records = []

	with open(filename) as f:
		rows = csv.reader(f)
		
		if has_headers:	
			headers = next(rows)

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

			if has_headers:
				if types:
					record = {k: f(v) for k, v, f in zip(headers, row, types)}
				else:
					record = {k: v for k, v in zip(headers, row)}
			else:
				if types:
					record = [t(r) for r, t in zip(row, types)]
					record = tuple(record)
				else:
					record = row 
				
			records.append(record)

	return records









