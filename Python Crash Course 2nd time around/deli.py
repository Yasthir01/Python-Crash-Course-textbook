sandwich_orders = ['chicken and mayo', 'pastrami', 'chicken tikka', 'grilled cheese',
				'turkey', 'pastrami', 'roast beef', 'pastrami']

finished_sandwiches = []

print("I'm sorry, we're out of Pastrami today :(")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"I'm working on your {current_sandwich.title()} sandwich")
	finished_sandwiches.append(current_sandwich)

print()
for sandwich in finished_sandwiches:
	print(f"I made a {sandwich} sandwich")