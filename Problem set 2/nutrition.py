def main():
    fruits = [
        {"name":"Apple","calories":"130"},
        {"name":"Avocado","calories":"50"},
        {"name":"Sweet Cherries","calories":"100"},
        {"name":"Grape Fruit","calories":"60"},
        {"name":"Strawberries","calories":"50"},
        {"name":"Kiwifruit","calories":"90"},
        {"name":"Pear","calories":"100"},
    ]

    item = input("Item: ").lower()
    for fruit in fruits:
        if fruit["name"].lower() == item:
            print(f"Calories: {fruit["calories"]}")
            break
main()
