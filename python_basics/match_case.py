# Pattern Matching Exercise

def main():
    # print("Hello, World!")
    print("Available operations include: add, sub, mul, div")
    operation = input("Enter an operation: ")
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    match operation:
        case 'add':
            result = number1 + number2
        case 'sub':
            result = number1 - number2
        case 'mul':
            result = number1 * number2
        case 'div':
            result = number1 / number2

    print(result)


if __name__ == "__main__":
    main()
