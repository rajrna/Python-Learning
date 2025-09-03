import csv

with open("family_second.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=[])