family_members = ['Mama', 'Papa', 'Ole', 'Johan', 'Mila', 'Theo']
family_ages = [36, 36, 15, 12, 9, 7]
family_members[1] = "Lars"
family_members.append("Hugo")
family_members.append("Momo")
del family_members[0]
family_members.insert(1, "Anni")

#family_members.sort(reverse=True)

for person in family_members[2:6]:
	message = "In meiner Familie ist"
	message += " "
	message += person
	print(message)

