#15
class Person:
	def __init__(self, firstName, lastName, age, email, middleName=''):
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
		self.email = email
		self.middleName = middleName

	def displayInfo(self):
		if (self.middleName):
			print(f"Name: {self.firstName} {self.middleName} {self.lastName}")
			print(f"Age: {self.age}")
			print(f"Email: {self.email}\n")
		else:
			print(f"Name: {self.firstName} {self.lastName}")
			print(f"Age: {self.age}")
			print(f"Email: {self.email}\n")


#16
person1 = Person('john','wick',25,'jwick@gmail.com')
person2 = Person('will','smit',52,'smit@gmail.com', 'jerry')

person1.displayInfo()
person2.displayInfo()