numbers = [1, 2, 3, 4, 5]

# squares_dict -> 1:1, 2:4, 3:9
squares_dict = {number : number **2 for number in numbers}
print(squares_dict)

even_squares_dict = {number : number **2 for number in numbers if number % 2 == 0}
print (even_squares_dict)

def square(number):
    return number ** 2

sq_dict = {number: square(number) for number in numbers}
print(sq_dict)