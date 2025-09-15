import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#to check the first two characters
def check_st_letters(s):
    start_letter = s[0:2]
    if start_letter.isalpha():
        return True

#to check the length of input
def check_len(s):
    if 2<= len(s) <=6:
        return True

#to check locations of numbers
def check_location(s):
    # Find first digit index
    digit_index = len(s)  # default means no digits found
    for i, char in enumerate(s):
        if char.isdigit():
            digit_index = i
            break

    # Letters before digits
    if not all(ch.isalpha() for ch in s[:digit_index]):
        return False

    # Digits after digits start
    if not all(ch.isdigit() for ch in s[digit_index:]):
        return False

    # First digit not zero
    if digit_index < len(s):
        if s[digit_index] == '0':
            return False

    return True

#to check if invalid characters are present
def check_symbols(s):
    for char in s:
        if char not in string.punctuation:
            return True


def is_valid(s):
    if(check_st_letters(s) and check_len(s)):
        if(check_location(s) and check_symbols(s)):
            return True
       
main()
