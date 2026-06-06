for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print("\n")

print("-" * 31)

for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")
print("\n")

for i in range(10):
    if i == 50:
        break
    print(i, end=" ")
else:
    print("Loop ended normally")

# Real use-case scenario

#List of fruits
fruits = ["Banana", "Orange", "Mango", "Grapes"]

# fruit we want to check
fruit_to_check = "Orange"

for fruit in fruits:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} is in your list.")
        break
else:
    print(f"{fruit_to_check} is NOT in your list.")

# ---------------------------
# List of fruits
fruits = ["Banana", "Orange", "Mango", "Grapes"]

# fruit we want to check
fruit_to_check = "Orange"

if fruit_to_check in fruits:
    print(f"{fruit_to_check} found")
else:
    print(f"{fruit_to_check} NOT found")

# One-liner conditional check
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} your list")