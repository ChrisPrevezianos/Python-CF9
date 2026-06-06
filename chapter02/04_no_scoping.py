import random

random_numbers = []

# for i in range(10):
#     num = random.randint(1, 100)
#     random_numbers.append(num)

for _ in range(10):
    num = random.randint(1, 100)
    random_numbers.append(num)

print(random_numbers)

# for num in random_numbers:
#     if num % 2 == 0:
#         even = num
#         name = "Katerina"

# print(f"Even: {even}")
# print(name)
# print(num)

# Find the last even number in the list
for num in random_numbers:
    if num % 2 == 0:  # Check if the number is even
        even = num  # Store the current even number

# Print the last number in the list (regardless of even or odd)
print(f"The last item of the list: {num}")

# Print the last even number encountered in the loop
print(f"The last 'even' item of the list: {even}")

