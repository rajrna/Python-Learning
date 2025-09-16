def main():
    ans = round(get_fraction()*100)
    if ans >=99:
        print("F")
    elif ans <= 1:
        print("E")
    else:
        print(f"{ans}%")


def get_fraction():

    while True:
        try:
            fract = input("Fraction: ")
            fract_list = fract.split("/")
            x,y = fract_list
            x = int(x)
            y = int(y)

            if x>y or x<0:
                continue
            ans = (x / y)
            return ans
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
