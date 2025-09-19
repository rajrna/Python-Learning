def main():
    u_input = input("Input: ")
    output = shorten(u_input)
    print(output)

def shorten(word):
    vowels = ["a", "i", "o", "u"]
    result = ""
    for char in word:
        if char.isalpha() and char not in vowels:
            result += char
    return result.upper()

if __name__ == "__main__":
    main()
