students = "Alice", "Bob", "Charlie"

print(type(students))

# iterate over a tuple
for index, value in enumerate(students):
    print(f"{index} : {value}")

# enhanced for
for st in students:
    print(st, end=', ')
print()

# Unpacking tuple elements into variables
first_st, second_st, third_st = students # ("Alice", "Bob", "Charlie")

print(f"first_st: {first_st}")
print(f"second_st: {second_st}")
print(f"third_st: {third_st}")

print(f"Second student: {students[1]}")
students = list(students) #typecast σε list
students[1] = "Panagiotis"
students = tuple(students)

print(students)
print(type(students))