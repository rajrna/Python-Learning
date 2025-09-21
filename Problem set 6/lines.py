import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(filename) as file:
        lines = file.readlines()

    count = 0
    for line in lines:
        stripped_line = line.strip()

        # Skip empty lines
        if not stripped_line:
            continue

        # Skip comment-only lines
        if stripped_line.startswith("#"):
            continue

        count += 1

    print(count)

except FileNotFoundError:
    sys.exit("File does not exist")
