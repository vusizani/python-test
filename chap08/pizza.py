def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	print("\nToppings:")
	for topping in toppings:
		print(f"\t{topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')