from random import choice


def get_winning_ticket(possibilities):
	"""Returning a winning ticket from a list of possibilites"""
	winning_ticket = []

	#We don't want to repeat items so we will use a while loop.
	while len(winning_ticket) < 4:
		pulled_item = choice(possibilities)

		# We have to make sure that no items are repeated
		if pulled_item not in winning_ticket:
			winning_ticket.append(pulled_item)

	return winning_ticket

def check_ticket(played_ticket, winning_ticket):
	"""Check all elements in the played ticket. If they are
	not in the winning ticket, return False.
	"""
	for element in played_ticket:
		if element not in winning_ticket:
			return False

	#We have to have a winning ticket
	return True


def make_random_ticket(possibilities):
	"""return a random ticket from a set of possibilites"""
	ticket = []
	#We don't want to repeat numbers or letters so we use a while loop.
	while len(ticket) < 4:
		pulled_item = choice(possibilities)

		# Only add the pulled item to the list if it hasn't already been pulled
		if pulled_item not in ticket:
			ticket.append(pulled_item)

	return ticket


#List of possibilities.
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

#Let's set a max number of tries in case this takes forever.
max_tries = 1_000_000

while not won:
	new_ticket = make_random_ticket(possibilities)
	won = check_ticket(new_ticket, winning_ticket)
	plays += 1
	if plays >= max_tries:
		break

if won:
	print("We have a winning ticket!")
	print(f"Your ticket: {new_ticket}")
	print(f"Winning ticket: {winning_ticket}")
	print(f"It only took {plays} tries to win!")

else:
	print(f"Tried {plays} times, without pulling a winner :(")
	print(f"Your ticket: {new_ticket}")
	print(f"Winning ticket: {winning_ticket}")




