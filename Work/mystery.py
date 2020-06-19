
# Since bool() returns True if its arg is not 0, and False if it is,
# then also since a string isn't considered the int 0, result is True.

result = bool("False")
print(result)

result = bool(0)	# False
print(result)
result = bool(1)	# True
print(result)

result = bool(1.73)	# True
print(result)

# Essentially, anything not explicitly a 0 returns True.



