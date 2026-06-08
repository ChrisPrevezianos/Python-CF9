items = [1, 2, 3.14, True, "Hello CF9 friends"]

for item in items:
    print(item, end=' ')
print()

# Nested list
# new_list = [[1, 2], [3, 4], [5, 6]]

new_list = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print(f"New List: {new_list}")

print(f"second nested list: {new_list[1]}") 
print(f"first element of second nested list: {new_list[1][0]}")

# [[3, 4], [1, 2]]
print(new_list[1], new_list[0]) 

print(new_list[:2][::-1])

# double for (HW)
# iterate the elements of new_list



