class Employees:
	def __init__(self, firstName, lastName, ID, email, address=''):
		self.firstName = firstName
		self.lastName = lastName
		self.ID = ID
		self.email = email
		self.address = address

	def displayInfo(self):
		if (self.address):
			print(f"Name: {self.firstName} {self.lastName}")
			print(f"ID: {self.ID}")
			print(f"Email: {self.email}")
			print(f"Address: {self.address}\n")
		else:
			print(f"Name: {self.firstName} {self.lastName}")
			print(f"ID: {self.ID}")
			print(f"Email: {self.email}\n")

	def changeEmail(self, newEmail):
		self.email = newEmail