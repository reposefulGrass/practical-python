# bounce.py
#
# Exercise 1.5

bounce = 1
height = 100.0

while bounce <= 10:
	height *= (3.0/5.0)
	print(bounce, round(height, 4))
	bounce += 1

	
