
bill_thickness = 0.011 * 0.01 	# 0.011 cm = 0.00011 m
tower_height = 442.1			# 442.1 m

day = 1
num_bills = 1

print("day #bills height")
while (num_bills * bill_thickness) < tower_height:
	print(day, num_bills, round(num_bills * bill_thickness, 5))
	num_bills *= 2
	day += 1

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', round(num_bills * bill_thickness, 5))

