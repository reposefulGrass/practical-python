# mortgage.py 
#
# Exercise 1.7

principal = 500000.0	# $500,000
rate = 0.05				# 5% 
payment = 2684.11		# $2684.11
total_paid = 0.0
month = 0

start_month = 60
end_month = 108
extra_payment = 1000

while principal > 0:
	if month > start_month and month < end_month: 
		actual_payment = payment + extra_payment
	else:
		actual_payment = payment

	principal = principal * (1 + rate / 12) - actual_payment;
	total_paid += actual_payment
	month += 1

	print(month, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', month)
