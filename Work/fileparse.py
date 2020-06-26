# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv (filename, select=[], types=[], has_headers=True):
	''' Parse a csv file into a list of records '''

	records = []

	if select and not has_headers:
		print('Error: Cannot use both has_headers=False and select')
		return None

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

			# reduce the columns in the row and types to only those selected
			if select:
				row = [row[index] for index in indices]
				if types:
					types = [types[index] for index in indices]

			# if the file has headers, use the headers as keys to columns
			if has_headers:
				if types:
					record = {k: f(v) for k, v, f in zip(headers, row, types)}
				else:
					record = {k: v for k, v in zip(headers, row)}
			# otherwise, return the row of columns as a tuple
			else:
				if types:
					record = tuple([t(r) for r, t in zip(row, types)])
				else:
					record = row 
				
			records.append(record)

	return records









