def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            in_date = input("Date: ")
            if "/" in in_date:
                month, day, year = in_date.split("/")
                month, day, year = int(month), int(day), int(year)
            elif "," in in_date:
                month_name, day_year = in_date.split(" ",1)
                month = months.index(month_name)+1
                day, year = day_year.split(",")
                day, year = int(day), int(year)
            else:
                raise ValueError

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
            else:
                continue

        except ValueError:
            pass
        # except IndexError:
        #     break
main()

