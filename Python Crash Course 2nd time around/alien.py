alien_0 = {'color': 'green', 'points': 5 }

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_00 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_00['x_position']}")

#Move the alien to the right.
#Determine how far to move the alien based on its curent speed.
if alien_00['speed'] == 'slow':
	x_increment = 1
elif alien_00['speed'] == 'medium':
	x_increment = 2
else:
	#This must be a fast alien
	x_increment = 3

#The new position is the old position plus the increment.
alien_00['x_position'] += x_increment

print(f"New position: {alien_00['x_position']}")