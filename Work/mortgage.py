# mortgage.py 
#
# Exercise 1.7

principal = 500000.0	# $500,000
rate = 0.05				# 5% 
payment = 2684.11		# $2684.11
total_paid = 0.0
month = 0

while principal > 0:
	if month < 12:
		actual_payment = payment + 1000
	else:
		actual_payment = payment

	principal = principal * (1 + rate / 12) - actual_payment;
	total_paid += actual_payment
	month += 1

print('Total paid', round(total_paid, 3))
