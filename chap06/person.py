person1 = {'name':'john','surname':'wick','age': 36}

print(f"NAME: {person1['name'].title()},")
print(f"SURNAME: {person1['surname'].title()},")
print(f"AGE: {person1['age']}")

person1['email'] = 'jwick@yahoo.com'
person1['male'] = True

print(f"EMAIL: {person1['email']}")
print(f"MALE: {person1['male']}")

person1['age'] = 30
del person1['male']

print(person1)

# info = person1['surname'].title()
# print(f"This person's surname is {info}.")

# info2 = person1.get('email', 'No email address found.')
# print(info2)

print('\nKey-Value Pairs:')
for k, v in person1.items():
	print(f"\t{k}: {v}")

print('\nValues:')
for v in person1.values():
	print(f"\t{v}")

print('\nKeys:')
for k in person1.keys():
	print(f"\t{k}")



