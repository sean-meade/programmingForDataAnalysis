# Squares

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in l:
	print("next is:")
	print(i)
	print(i*i)
	print("")

print("That's the whole list.")

for i in range(10):
	# f treats the string as special
	print(f"{i:2} {i*i:3} {i*i*i:4}")

print(range(20))
print(list(range(20)))