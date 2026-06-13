def is_armstrong(n: int) -> bool:
    digits = str(n)
    power = len(digits)
    total = 0
 
    for digit in digits:
        total += int(digit) ** power
 
    return n == total
 
def main():
    try:
        num = int(input("Please enter an int: "))
    except ValueError:
        print("Pleas enter a valid int.")
        return
   
    if is_armstrong(num):
        print(f"{num} is Armstrong number")
    else:
        print(f"{num} is NOT Armstrong number")
 
if __name__ == "__main__":
    main()