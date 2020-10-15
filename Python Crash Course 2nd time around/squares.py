squares = []
for value in range(1, 11):
	squares.append(value**2)

print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares2 = [value**2 for value in range(1,11)]
print(squares2)

for number in range(1,21):
	print(number)

million = list(range(1, 1_000_001))
print(max(million))

odd_numbers = list(range(1, 21, 3))
for odd in odd_numbers:
	print(odd)
print()
threes = list(range(3, 31, 3))
for multiple in threes:
	print(multiple)

print()

cubes = []
for cube in range(1,11):
	cubes.append(cube**3)
print(cubes)

cubes2 = [cube**3 for cube in range(1,11)]
print(cubes2)


