
guests = {}
def add_contacts(name,email):
	if name in guests.keys():
		print(guests[name])
	else:
		guests[name] = email

command = input("Enter command:")
while command != "quit":
	name = input("Enter name:")
	email = input("Enter email:")
	add_contacts(name,email)
	print (guests)

	command = input("Enter command:")





