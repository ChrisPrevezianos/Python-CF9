def is_square(length:int, width:int) -> bool:
    """Check if rectange is square..."""
    return length == width
 
# def my_add(a, b):
#     return a + b
 
def main():
    # print(my_add(100, 200)) # 300
    # print(my_add("Hello", " CF9 friends"))
 
    try:
        legth = int(input("Give me the legth of the rectangle: "))
        width = int(input("Give me the width of the rectange: "))
    except ValueError:
        print("Invalid input. Please enter valid integers for length and width.")
        return
 
    if is_square(legth, width):
        print("The rectangle is square")
    else:
        print("The rectangle is NOT square")
 
    pass
 
if __name__ == '__main__':
    main()

