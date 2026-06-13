def compare_integers(a, b):
    if a == b:
        print("The numbers are equal.")
    elif a > b:
        print("The first number is greater than the second number.")
    else: # a <= b
        print("The first number is less than the second number.")

def main():
    try:
        a = int(input("Please enter the first number to compare: "))
        b = int(input("Please enter the second number to compare: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
    compare_integers(a, b)

    #1. Ternary operator (simple example)
    result = "positive" if a > 0 else "non-positive"
    print(result)

    
    # print("The numbers are equal.")
    # print("The first number is greater than the second number.")
    # print("The first number is less than the second number.")

    # 2.  Ternary operator (extented example)


    result = (
        "The numbers are equal." if a == b else
        "The first number is greater than the second number." if a > b else
        "The first number is less than the second number."
    )
    print(result)

if __name__ == "__main__":
    main()