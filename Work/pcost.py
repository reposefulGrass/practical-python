# pcost.py
#
# Exercise 1.27

def portfolio_cost (filename):
	'Read the file \'filename\', then calculate the total cost.'

	total_cost = 0.0

	with open(filename, 'rt') as f:
		headers = next(f)

		for line in f:
			try:	
				row = line.split(',')
				total_cost += (int(row[1]) * float(row[2].strip()))
			except ValueError:
				print("ParseError:", line.strip())

	return total_cost

cost = round(portfolio_cost('Data/missing.csv'), 2)
print('Total cost', cost)

