members = []

with open("german_family.csv") as file :
    for line in file:
        noun, pronoun = line.rstrip().split(",")
        members.append(f"{pronoun} ,{noun}")

for member in sorted(members):
    print(member)
    