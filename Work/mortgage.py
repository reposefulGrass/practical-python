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

while (principal - payment) > 0:
	principal = principal * (1 + rate / 12) - payment;
	total_paid += payment
	month += 1

	if month > start_month and month < end_month: 
		principal -= extra_payment
		total_paid += extra_payment

	print(f'{month:>4d} {total_paid:>9.2f} {principal:>9.2f}')

print('Total paid', round(total_paid, 2))
print('Months', month)
