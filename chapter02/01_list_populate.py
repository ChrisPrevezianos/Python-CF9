ages = [19, 23, 34, 45]

print("Initial list of ages:", ages)

# Read: Iterating over a list with enhanced for
for age in ages:
    print(age, end=" ")
print()

# Read: Iterating over a list using enumerate -> (index, value)
# for index, value in enumerate(ages):
#     print(f"Index: {index}, value:{value}")

products = ["Melon", "Banana", "Fig", "Orange"]
for index, value in enumerate(products, start=1):
    print(f"{index}. {value}")

# Python's loop variables persist after the loop ends
print(f"\nVariable 'age' after the loop: {age}")