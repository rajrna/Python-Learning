from random import randint

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            continue

    ans = randint(1, n)

    while True:
        try:
            re = int(input("Guess: "))
            if re < 1:
                continue
            if re > ans:
                print("Too large!")
            elif re < ans:
                print("Too small!")
            else:
                print("Just right!")
                break
        except ValueError:
            continue

if __name__ == "__main__":
    main()
