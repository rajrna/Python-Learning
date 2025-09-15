def main():
    user_input = input("Input: ")
    output = ""
    vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]

    for char in user_input:
        if char not in vowels:
            output += char

    print(output)

main()
