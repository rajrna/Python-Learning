menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0
    while True:
        try:
            order = input("Item: ").lower()
            for item in menu:
                if order == item.lower():
                    total += menu[item]
                    print(f"Total: ${total:.2f}")
        except ValueError:
            pass
        except KeyError:
            pass
        except EOFError:
            print("")
            break
main()
