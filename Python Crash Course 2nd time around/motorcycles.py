motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles.insert(1, 'yamaha')
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

print(motorcycles)
motorcycles.append('suzuki')
print(motorcycles)

#Print a statement about the last motorcycle I owned and pop it
last_owned = motorcycles.pop()
print(f"The last motorcyle I owned was a {last_owned.title()}.")

print(motorcycles)
#Let's add Suzuki back to the list
motorcycles.append('suzuki')
print(motorcycles)

#Pop out the first item and assign it to first_owned
first_owned = motorcycles.pop(0)
print(f"The first motorcyle I owned was a {first_owned.title()}.")

print(motorcycles)
motorcycles.insert(0, 'honda')
print()
motorcycles.append('ducati')
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

print(f"\nA {too_expensive.title()} is too expensive for me!")

guests = ['Iron man', 'Superman', 'Batman']
for guest in guests:
	print(f"{guest}, please come to dinner!")