import csv

members= []

with open("family_second.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        members.append({"noun":row["noun"] , "pronoun":row["pronoun"]})


for member in sorted(members, key=lambda member: member["noun"]):
    print(f"{member["pronoun"]}, {member["noun"]}")        