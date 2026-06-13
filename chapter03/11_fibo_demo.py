def main():
    a = 0
    b = 1

    n = int(input("Please enter an integer: "))

    for i in range(2, n + 1):
        temp = a
        a = b
        b = temp + b
    
    print(f"The {n}th fibo number is: {b}")


if __name__ == "__main__":
    main()