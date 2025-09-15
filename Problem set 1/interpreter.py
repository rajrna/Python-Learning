def get_ans():
    expression = input("Expression : ")
    x,y,z = expression.split()
    x = float(x)
    z = float(z)

    match y:
        case "+":
            return x+z
        case "-":
            return x-z
        case "*":
            return x*z
        case "/":
            return x/z

def main():
    result = get_ans()
    print(result)

if __name__ == "__main__":
    main()