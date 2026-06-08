fruits = ["Apple", "Banana", "Cherry", "Apple"]

print("Initial list of fruits:", fruits)

# Add a single element at the end of the list
fruits.append("Berry")
print(f"After adding Berry: {fruits}")

#Add multiple elements at the end of the list
fruits.extend(["Grapes", "Fig"])
print(f"After adding Grapes and Fig:", fruits)

# fruits.extend("Panos")
# print(f"Don't do that: {fruits}")

# fruits.extend(["Panos"])
# print(f"Don't do that: {fruits}")

# insert an element at a specific position
fruits.insert(1, "Coconut")
print(f"List after inserting Coconut at index 1: {fruits}")

#Update the first element
fruits[0] = "Mellon"
print(f"After updating element at index 0: {fruits}")

# Updating with slicing
# fruits[1:3] = ["Katerina", "Eleni", "Kostas"] # 'Coconut', 'Banana'
# print(fruits)

# Delete an element by position
f = fruits.pop(2)
print(f)
print(fruits)

# Delete an element using its name: remove()
fruits.remove("Cherry")
print(f"List after removing Cherry: {fruits}")

fruits_to_remove = "MagicFruit"

if fruits_to_remove in fruits:
    fruits.remove(fruits_to_remove)
else:
    print(f"{fruits_to_remove} not in the list")

# Search for an element in the list
pos = fruits.index("Berry")
print(f"Berry has index: {pos}")