import csv
members = []

with open("german_family.csv") as file :
    reader = csv.reader(file)
    for noun, pronoun in reader:
        members.append({"noun":noun,"pronoun" :pronoun })
# def get_noun(member):
    # return member['noun']

# First use of lambda function
for member in sorted(members, key=lambda member: member['noun']):
    print(f"{member['pronoun']} , {member['noun']}") 