file_path = 'data/pi_digits.txt'

with open(file_path) as file_object:
	files = file_object.readlines()

pi_string = ''
for line in files:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))


# file_path = 'data/pi_digits.txt'

# with open(file_path) as file_object:
# 	lines = file_object.readlines()

# pi_string = ''
# for line in lines:
# 	pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))