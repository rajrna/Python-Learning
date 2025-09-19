def main():
    while True:
        try:
            u_input = input("Fraction: ")
            percent = convert(u_input)
            gauge(percent)
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError("Can't divide by zero")
    elif x > y or x < 0:
        raise ValueError("Invalid Fraction")
    return (x / y) * 100


def gauge(percentage):
    if percentage >= 99:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(f"{int(percentage)}%")


if __name__ == "__main__":
    main()
