squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

for player in players[2:]:
	print(player.title())