def main():
    grocery_list = {}

    while True:
        try:
            grocery = input("").upper()
            if grocery in grocery_list:
                grocery_list[grocery] += 1
            else:
                grocery_list[grocery] = 1
        except EOFError:
            print("")
            sorted_list = sorted(grocery_list)
            for grocery in sorted_list:
                print(grocery_list[grocery], grocery)
            break

main()
