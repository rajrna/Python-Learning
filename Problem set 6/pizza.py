import sys
from tabulate import tabulate
import csv

if not len(sys.argv)==2:
    sys.exit("No argument provided")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Incorrect file extension")

menu_dict = sys.argv[1]
# >>> print(tabulate(table, headers, tablefmt="pretty"))
pizzas=[]
try:
    with open(f"{menu_dict}") as file:
        reader = csv.DictReader(file)
        for row in reader:
            pizzas.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(pizzas, headers ="keys",tablefmt="grid"))
