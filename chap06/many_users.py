users = {
'aeinstein': {
			'first': 'albert',
			'last': 'einstein',
			'location': 'princeton',
			},
'mcurie': {
			'first': 'marie',
			'last': 'curie',
			'location': 'paris',
			},
}


for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")



cars = {
'BMW': {
			'model': '5-series',
			'year': 2020,
			'milage': 12000,
			},
'Mercedes Benz': {
			'model': 'GLA',
			'year': 2019,
			'milage': 75000,
			},
}

for car, car_info in cars.items():
	print(f"\nCar: {car}")
	print(f"\tModel: {car_info['model']}")
	print(f"\tYear: {car_info['year']}")
	print(f"\tMilage: {car_info['milage']}")