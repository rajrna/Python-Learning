def main():
    time = input("What time is it? : ")
    time_in_dec = convert(time)

    if 7.00 <= time_in_dec <= 8.00:
        print("breakfast time")
    elif 12.00 <= time_in_dec <= 13.00:
        print("lunch time")
    elif 18.00 <= time_in_dec <= 19.00:
        print("dinner time")

def convert(time):
    hours,minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    time_in_dec = ((hours*60)+minutes)/60
    return time_in_dec


if __name__ == "__main__":
    main()
