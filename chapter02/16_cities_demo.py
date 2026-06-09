def print_cities(*cities: str, separator: str = ", ") -> None:
    """Homework"""
    if not cities:
        print("No cities provided")
    else:
        print("Cities:", separator.join(cities))

def main():
    print_cities("Athens", "Paris", "London", separator="\t")
    print("Athens", "Paris", "London", sep="\t")
    print()

if __name__ == "__main__":
    main()