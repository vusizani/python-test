class Dog:
	"""A simple attempt to model a dog."""
	def __init__(self, name, age, breed=''):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age
		self.breed = breed

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6, 'Husky')
your_dog = Dog('Harry', 10, 'Boereboel')

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()