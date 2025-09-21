import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Not enough arguments")

    read_file = sys.argv[1]
    write_file = sys.argv[2]

    students = []
    try:
        # read file
        with open(f"{read_file}", newline="") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                name = row["name"].strip('"')
                last, first = [part.strip() for part in name.split(",", 1)]
                house = row["house"]
                students.append({"first":first,"last":last,"house":house})
        # write to file
        with open(f"{write_file}" ,"w",newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames= ["first","last","house"])
            writer.writeheader()
            writer.writerows(students)

    except FileNotFoundError:
        sys.exit("File does not exist")

    for student in students:
        print(student)

if __name__ == "__main__":
    main()
