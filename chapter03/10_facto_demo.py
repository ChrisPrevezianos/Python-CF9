def calculate_facto(n: int) -> int:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
 
def main():
    print(f"6! = {calculate_facto(6)}")
 
if __name__ == "__main__":
    main()