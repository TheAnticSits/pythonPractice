

employee_file = open("employees", "r")

individual = (employee_file.readlines())

print(individual)


employee_file.close()

# "r" is for read
# "w" is for write
# "a" is for append