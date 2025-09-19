
def main():
    plate = input("Plate: ")
    # Always returns "Valid" regardless of the plate
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Bug: No checks are actually performed.
    return True  # Always returns True, even for invalid plates.

if __name__ == "__main__":
    main()
