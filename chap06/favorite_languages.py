favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

# language1 = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language1}.")

# langauge2 = favorite_languages.get('steve', 'No value assigned.')
# print(langauge2)

for key, value in favorite_languages.items():
	print(f"Key: {key.title()}, Value: {value.title()}")

print("\nAccessing keys:")
for key in favorite_languages.keys():
	print(f"Key: {key.title()}")

print("\nAccessing values:")
for value in set(favorite_languages.values()):
	print(f"Value: {value.title()}")