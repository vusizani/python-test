cars = ['audi', 'Bmw', 'subaru', 'toyota']

for car in cars:
	if (car.lower() == 'bmw') and (len(car) < 5):
		print(car.upper())
	else:
		print(car.title())

print("\n")

car = 'bmw'
result = (car == 'bmw')
print(result)